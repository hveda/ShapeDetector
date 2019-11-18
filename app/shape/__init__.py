"""Init file for shape class."""
from flask import current_app as app


def format_point(point):
    """Format point to list of integer."""
    formatted_point = ''.join(ch for ch in point if ch.isdigit())
    return int(formatted_point)


def format_line(line):
    """Format line to list of coordinat."""
    line = line.split('),')
    head = line[0].split(',')
    tail = line[1].split(',')
    head = [format_point(head[0]), format_point(head[1])]
    tail = [format_point(tail[0]), format_point(tail[1])]
    return [head, tail]


def is_valid_line(line):
    """Check if valid coordinat values."""
    for p in line:
        for i in p:
            if i < 0 or i > 100:
                return False
    return True


def build_shape(data):
    """Build shape from list of lines."""
    lines = data.get("lines")
    app.logger.info("Data payload: {}".format(lines))
    formatted_lines = []
    for line in lines:
        formatted_line = format_line(line)
        if is_valid_line(formatted_line):
            formatted_lines.append(formatted_line)
    app.logger.info("Data formatted: {}".format(formatted_lines))

    list_of_shape = []
    while len(formatted_lines) >= 3:
        app.logger.info("Lines before:")
        app.logger.info(formatted_lines)
        shape = Shape()
        shape.build(formatted_lines)
        for line in shape.lines:
            if line in formatted_lines:
                app.logger.info(line)
                formatted_lines.remove(line)
        list_of_shape.append(shape.__repr__())

        app.logger.info("Lines after:")
        app.logger.info(formatted_lines)
    return list_of_shape


class Shape:
    """Shape class."""

    def __init__(self):
        """Init shape object."""
        self.head = [0, -1]    # point of lines
        self.tail = [-1, 0]    # point of lines
        self.edge = []         # list of points/edges
        self.lines = []        # list of shape lines coordinat

    def __repr__(self):
        """Shape representation"""
        edge_dict = {
            3: "Triangle",
            4: "Quadliteral",
            5: "Pentagon"
        }
        vertices = ','.join('({}, {})'.format(v[0], v[1]) for v in self.edge)

        representation = {
            "Name": edge_dict.get(len(self.edge)),
            "Vertices": "[" + vertices + "]"
        }

        return representation

    def next_head(self, points):
        """Update start point of shape."""
        self.lines.append(points)
        if points[0] not in self.edge and points[0] == self.head:
            self.edge.append(self.head)
            self.head = points[1]
        elif points[1] not in self.edge and points[1] == self.head:
            self.edge.append(self.head)
            self.head = points[0]
        if points[0] in self.edge or points[1] in self.edge:
            self.lines.append(points)

    def next_tail(self, points):
        """Update end point of shape."""
        if points[0] not in self.edge and points[0] == self.tail:
            self.edge.append(self.tail)
            self.tail = points[1]
        elif points[1] not in self.edge and points[1] == self.tail:
            self.edge.append(self.tail)
            self.tail = points[0]
        if points[0] in self.edge or points[1] in self.edge:
            self.lines.append(points)

    def is_valid_shape(self):
        """Check if valid shape with minimum edge three."""
        if self.edge > 2:
            return True
        return False

    def is_valid_lines(self):
        """Remove unused line."""
        for line in self.lines:
            if line[0] not in self.edge or line[1] not in self.edge:
                self.lines.remove(line)

    def build(self, lines):
        """Build shape."""
        self.head = lines[0][0]
        self.tail = lines[0][1]
        self.lines.append(lines[0])
        for i in range(1, len(lines)):
            if lines[i][0] == self.head or lines[i][1] == self.head:
                self.next_head(lines[i])
            # change to checker if closing shape
            if self.head in self.edge and self.tail in self.edge:
                break
            if lines[i][0] == self.tail or lines[i][1] == self.tail:
                self.next_tail(lines[i])
            # change to checker if closing shape
            if self.head in self.edge and self.tail in self.edge:
                break

        # remove connected non-close shape line
        self.is_valid_lines()

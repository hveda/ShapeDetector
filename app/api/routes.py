"""Endpoints /save_emails."""
import json

from flask import request
from flask import current_app as app
from flask_restplus import Namespace, Resource, fields

from app.shape import build_shape

ns = Namespace('Shape Detection', description='Submit set of lines.', path='/')

"""
Serializer for swagger documentation.
As example using Singapore Standart Timezone (SST).
List of line coordinat separated by comma(s).
"""
lines = ns.model('ShapeDetector', {
    'lines': fields.List(fields.String(
        required=True,
        description='List of lines',
        example="(x1,y1), (x1,y1)"
    )),
})


@ns.route('/detect')
class ShapeApi(Resource):
    """Event api endpoints."""

    @ns.expect(lines, validate=True)
    @ns.doc(body='ShapeDetector', code=200)
    def post(self):
        """Detect shape from list of lines."""
        app.logger.info(request.json)
        shape = build_shape(request.json)
        shape = {"Shape": shape}
        return shape, 200

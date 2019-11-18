FROM python:3.6.9

MAINTAINER Heri Rusmanto "hvedaid@gmail.com"

# Set working directory
RUN mkdir -p /var/www/shape_detector
WORKDIR /var/www/shape_detector

# Add requirements (to leverage Docker cache)
ADD requirements.txt /var/www/shape_detector

# Install requirements
RUN pip install -r requirements.txt

ADD . /var/www/shape_detector

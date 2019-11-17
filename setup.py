"""Setup file."""
from setuptools import setup

setup(
    name='ShapeDetector',
    version='0.1.0',
    packages=['app'],
    url='https://github.com/hveda/shape_detector',
    author='Heri Rusmanto',
    author_email='hvedaid@gmail.com',
    description='Shape Detector API',
    keywords=['shape', 'detector', 'flask'],
    install_requires=[
        'flask>=0.10.1',
    ],
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6'
    ]
)

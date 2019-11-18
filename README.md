Shape Detector
=================

Simple shape detector API using flask.

## Setup

### Configuration
Rename .env.example to .env
And then set your variable there.

Quickly run the project using [docker](https://www.docker.com/) and
[docker-compose](https://docs.docker.com/compose/):
```bash
docker-compose up -d
```

## How to use

Go to http://0.0.0.0:5000/shape/doc

Or you can run in your terminal
```bash
curl -X POST "http://0.0.0.0:5000/shape/detect" 
-H "accept: application/json" 
-H "Content-Type: application/json" 
-d "{ \"lines\" : [\"(1,1),(2,2)\",\"(3,3),(2,2)\",\"(4,4),(3,3)\",\"(1,1),(4,4)\",\"(7,7),(8,8)\",\"(8,8),(9,9)\",\"(9,9),(7,7)\"]}"
```
 
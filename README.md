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
curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{ \ 
   "subject": "Email subject", \ 
   "content": "Email body", \ 
   "timestamp": "07 Feb 2018 00:06 +08", \ 
   "recipients": "user1%40mail.com, user2%40mail.com" \ 
 }' 'http://127.0.0.1:5000/api/save_emails'
 ```
 
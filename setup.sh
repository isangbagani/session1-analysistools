#!/usr/bin/bash

echo "127.0.0.1     session1.demo" >> /etc/hosts
echo "=> Building docker image ..."
docker build -t session1 . > /dev/null 2>&1
echo "=> docker build ... done"
docker rm session1 > /dev/null 2>&1
echo "=> docker container clean-up ... done"
docker run -d -p 8000:8000 --name session1 session1 > /dev/null 2>&1
echo "=> docker run ...done"
echo "=> App can be found in http://session1.demo:8000"
#!/usr/bin/bash

echo "=> Removing the container and image"
docker stop session1 > /dev/null 2>&1
docker rm session1 > /dev/null 2>&1
docker rmi session1 > /dev/null 2>&1
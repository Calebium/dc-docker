#!/usr/bin/env bash

# Run this shell script to build the docker image for DeepCell

docker build -t calebium/dc-docker -f Dockerfile.DeepCell \
       --build-arg USERNAME=$(id -un) --build-arg GROUPNAME=$(id -gn) --build-arg UID=$(id -u) --build-arg GID=$(id -g) \
       .

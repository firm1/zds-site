#!/bin/bash

DOCKER_IMAGE=$1
DOCKER_NAME=$2
DOCKER_VERSION=$3

if [ -z "$DOCKER_NAME" ]; then
    echo "We need a docker image name"
    exit 1
fi

if [ -z "$DOCKER_VERSION" ]; then
    echo "We need a docker version"
    exit 1
fi

if [ -z "$DOCKER_USER" ]; then
    if [ -z "$4" ]; then
        echo "Please provide docker username registry hub"
        exit 1
    else
        DOCKER_USER="$4"
    fi
fi

if [ -z "$DOCKER_PASSWORD" ]; then
    if [ -z "$5" ]; then
        echo "Please provide docker password registry hub"
        exit 1
    else
        DOCKER_PASSWORD="$5"
    fi
fi

echo "Tag docker image"
docker tag "$DOCKER_IMAGE" "firm1/$DOCKER_NAME:$DOCKER_VERSION"

echo "Login to registry hub"
docker login -u $DOCKER_USER -p $DOCKER_PASSWORD

echo "Push docker image"
docker push "firm1/$DOCKER_NAME"

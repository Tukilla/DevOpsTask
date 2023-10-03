#!/bin/bash

# Pull the latest Docker image from Docker Hub
docker pull tukilla/pythonapp:latest

# Run the Docker container, exposing it on port 8080
docker run -d -p 8080:80 --name pythonapp tukilla/pythonapp:latest


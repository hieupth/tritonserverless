#!/bin/bash

# Define environment variables
export BASE_IMAGE="python:3.9-slim"
export DOCKER_ARG_VARS="ENV_VAR1,ENV_VAR2"

# Run the Python script
python3 generate_dockerfile.py
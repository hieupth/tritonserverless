# pykc

## Script create Dockerfile.serverless
1. create conda env
```
conda create -n severless python=3.10
```

2. run `scripts/create_dockerfile.sh`, note that change your image and environment variables such as `TOKEN`

```bash
# Define environment variables
export BASE_IMAGE="python:3.9-slim"
export DOCKER_ARG_VARS="ENV_VAR1,ENV_VAR2"
export RUN_SCRIPT="start.sh"

# Run the Python script
python3 generate_dockerfile.py
```

3. commit to build workflow with github action
- add secret tokens, repo model to clone

import os
import sys
import jinja2

# This script generates a Dockerfile for a serverless deployment.
base_image = os.getenv("BASE_IMAGE", None)
docker_arg_vars = os.getenv("DOCKER_ARG_VARS", None)
run_script = os.getenv("RUN_SCRIPT", "script.sh")

# check
assert base_image is not None, "`BASE_IMAGE` is not set"
assert docker_arg_vars is not None, "`DOCKER_ARG_VARS` is not set"

# define template
template_text = """
FROM {{ base_image }} as builder
{% for arg in arg_var %}
ARG {{ arg }}{% endfor %}
{% for arg in arg_var %}
ENV {{ arg }}=${{ arg }}{% endfor %}

RUN apt-get update && apt-get install -y
RUN pip install -r requirements.txt
RUN python3 hf.py

FROM {{ base_image }} as runner

COPY --from=builder /models /models
COPY --from=builder /venv /venv

RUN chmod +x {{ run_script }}
CMD ["./{{ run_script }}"]
"""

# "abc,abc => ['abc', 'abc']"
docker_arg_vars = docker_arg_vars.split(",")

# render template
template_text = jinja2.Template(template_text)
template_text = template_text.render(
    base_image=base_image,
    arg_var=docker_arg_vars,
    run_script=run_script
)

# write to file
current_directory = os.getcwd()
os.makedirs(os.path.join(current_directory, "dockerfiles"), exist_ok=True)
with open(os.path.join(current_directory, "dockerfiles", "Dockerfile.serverless"), "w") as f:
    f.write(template_text)
    print("Generated Dockerfile:", os.path.join(current_directory, "dockerfiles", "Dockerfile"))
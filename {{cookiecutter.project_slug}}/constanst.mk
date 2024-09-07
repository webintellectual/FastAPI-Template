# Make sure to run command 'make refactor' after changing these values here.

PYTHON_VERSION:={{cookiecutter.python_version}}

# aka the project name and root directory name:
PROJECT_SLUG:={{cookiecutter.project_slug}}

# inner folder name:
PACKAGE_NAME:={{cookiecutter.package_name}}

IMAGE_NAME:=$(PROJECT_SLUG)-img
CONTAINER_NAME:=$(PROJECT_SLUG)

CONTAINER_PORT:=8540
HOST_PORT:=8540
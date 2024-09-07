FROM python:{{cookiecutter.python_version}}

# install poetry
RUN pip install poetry

# set working directory
WORKDIR /{{cookiecutter.project_slug}}

# copy the poetry files
COPY . .

# enter poetry environment
RUN poetry config virtualenvs.create false

# install dependencies
RUN poetry install

# expose port
EXPOSE 8540

# run the app
CMD ["make", "start-server"]
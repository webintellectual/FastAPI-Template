from fastapi import FastAPI
from {{cookiecutter.package_name}}.routers import tests
# from {{cookiecutter.package_name}}.routers import items

app = FastAPI()

app.include_router(tests.router)
# app.include_router(items.router)
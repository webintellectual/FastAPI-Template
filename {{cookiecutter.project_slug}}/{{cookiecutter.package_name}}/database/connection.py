from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL")

{% if cookiecutter.database_application == 'sqlite' %}
DATABASE_URL = DATABASE_URL or "sqlite:///./{{cookiecutter.project_slug}}.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
{% elif cookiecutter.database_application == 'postgresql' %}
DATABASE_URL = DATABASE_URL or "postgresql://user:password@localhost:5432/{{cookiecutter.project_slug}}"
engine = create_engine(DATABASE_URL)
{% elif cookiecutter.database_application == 'mysql' %}
DATABASE_URL = DATABASE_URL or "mysql+pymysql://user:password@localhost:3306/{{cookiecutter.project_slug}}"
engine = create_engine(DATABASE_URL)
{% endif %}

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

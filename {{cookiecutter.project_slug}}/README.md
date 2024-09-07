# Pre-requisites
1. Python
2. [Poetry](https://python-poetry.org/) (Dependencies manager)
3. Docker

# Database Connection Set up
Create .env file in the root directory and make DATABASE_URL variable there and provide the value.
    - POSTGRES_DB (Name of the postgres database you want to connect with your FastAPI app)
    - POSTGRES_USER (Username of database)
    - POSTGRES_PASSWORD (password of database)
    - POSTGRES_HOST (IP Address or Domain of the machine where the database is hosted. Use public IP Address. Internal IP will work only if your FastAPI app is in same network as database)
    - POSTGRES_PORT (Port number of the machine where database is hosted)


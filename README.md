# FastAPI_Tutorial
## create a environment
`python3 -m venv env_name`
## install FastAPI and its dependencies:
`pip install fastapi[all]`
## Run docker compose
`docker-compose up`
## Installing the UUID OSSP PostgreSQL Extension
`docker exec -it postgres bash`
`psql -U postgres fastapi`
`CREATE EXTENSION IF NOT EXISTS "uuid-ossp";`
## Password Management
`pip install "passlib[bcrypt]"`
## Configure the FastAPI JWT Auth Extension
`pip install 'fastapi-jwt-auth[asymmetric]'`
## install SQLAlchemy and psycopg2 to connect to PostgreSQL
`pip3 install psycopg2-binary sqlalchemy`
## Database Migration with Alembic
`pip install alembic`
## create a migration environment 
`alembic init alembic`
`alembic upgrade head`
## start the FastAPI server with the command line:
`uvicorn app.main:app --host localhost --port 8000 --reload`




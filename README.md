# goit-pythonweb-hw-06

- start Docker;
- launch the container with Postgess and create database or use the default;
- apply/migrate schema using Alembic;
- seed database with dummy data;
- execute sqls or work with interactive console.

# Docker

docker run --name my_postgres_task_06 -e POSTGRES_PASSWORD=567234 -p 5432:5432 -d postgres
docker exec -it my_postgres_task_06 psql -U postgres
CREATE DATABASE mydatabase;
\q

# Alembic

alembic init migrations
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head

# List all tables in DB

docker exec -it my_postgres_task_06 psql -U postgres -d mydatabase -c "\dt"

# Seed Database

python -m app.seed

# Execute selects

to run select queries use: python -m app.main --mode ExecuteQueries

# Interactive console

to modify database using terminal run: python -m app.main --mode ModifyDatabase

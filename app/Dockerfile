# Dockerfile

# pull the official docker image
FROM python:3.10-buster

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# run migrations and startup process, sleep 3 secs for DB initialization.
CMD ["sh", "-c", "sleep 3 && alembic upgrade head && uvicorn main:app --host 0.0.0.0"]
# copy project
COPY . .
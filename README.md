# TYPETONE TEST


## About
This is a Tech Task solution:
```
Create a webservice in python which can shorten urls like TinyURL and bit.ly. You can use any
Rest API framework you prefer. FYI: At Typetone we use FastAPI.
```

## Project Setup
```
clone this project
cd to this project folder
```
#### ENVs
```
create .env file in root of the project
set env variables by your use cases, or just copy and paste bellow data (for test purpose):

POSTGRES_DB=typetone_db
POSTGRES_PORT=5432
POSTGRES_PASSWORD=DvzYuJt4MeLmbqT3fyXKk8
POSTGRES_USER=typetone_user
DATABASE_URL="postgresql+psycopg2://typetone_user:DvzYuJt4MeLmbqT3fyXKk8@db:5432/typetone_db"
```
#### Build and run
```
docker-compose build
docker-compose up
```
## Endpoints
```
POST - http://127.0.0.1:8000/shorten
GET - http://127.0.0.1:8000/<shortcode>
GET - http://127.0.0.1:8000/<shortcode>/stats

http://127.0.0.1:8000/docs -> SWAGGER documentation
```

## Tests
```
docker-compose run web python -m pytest -s
```
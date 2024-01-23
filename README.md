docker-compose run web alembic revision --autogenerate -m "First migration"

docker-compose run web alembic upgrade head

docker-compose run web python -m pytest -s

MIGRATIONS_DB_CONFIG = mspy_room/db/alembic.ini

.PHONY: migrate
migrate:
	uv run alembic upgrade head

.PHONY: downgrade
downgrade:
	uv run alembic downgrade -1

.PHONY: migrations
migrations:
	uv run alembic revision --autogenerate --message auto

.PHONY: fmt
fmt:
	uv run ruff check --fix app/
	uv run ruff format app/


.PHONY: lint
lint:
	uv run ruff check .
	uv run ruff format --check --diff .


.PHONY: test
test:
	uv run pytest $(opts) $(call tests,.)


.PHONY: start
start:
	uv run uvicorn main:app --reload


.PHONY: docker-build
docker-build:
	docker build -t comment_generator .


.PHONY: docker-start
docker-start:
	docker run --network host --env-file .env -it comment_generator:latest

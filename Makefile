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

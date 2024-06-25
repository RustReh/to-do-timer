.DEFAULT_GOAL := help

run: ## Run app
	poetry run uvicorn main:app --host 0.0.0.0 --port 8000 --reload --env-file .prod.env

install: ## Installing lib
	poetry add $(LIBRARY)

migrate-create: ## Migrating
	alembic revision --autogenerate -m $(MIGRATION)

migrate-apply: ## Migrating
	alembic upgrade head

uninstall: ## Uninstalling lib
	poetry remove $(LIBRARY)
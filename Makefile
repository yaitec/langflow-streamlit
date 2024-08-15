.PHONY: lint test start start-streamlit-only


clean_python_cache:
	@echo "Cleaning Python cache..."
	find . -type d -name '__pycache__' -exec rm -r {} +
	find . -type f -name '*.py[cod]' -exec rm -f {} +
	find . -type f -name '*~' -exec rm -f {} +
	find . -type f -name '.*~' -exec rm -f {} +
	@echo "$(GREEN)Python cache cleaned.$(NC)"

## help: Show this help info.
help: Makefile
	@printf "\n\033[1mUsage: make <TARGETS> ...\033[0m\n\n\033[1mTargets:\033[0m\n\n"
	@sed -n 's/^## //p' $< | awk -F':' '{printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' | sort | sed -e 's/^/  /'

## start: Starts langflow, streamlit and streamlit api.
start:
	poetry install
	poetry run python server.py

## start-streamlit-only: Starts streamlit and streamlit api.
start-streamlit-only: clean_python_cache
	@echo "Cleaning Python cache..."
	find . -type d -name '__pycache__' -exec rm -r {} +
	find . -type f -name '*.py[cod]' -exec rm -f {} +
	find . -type f -name '*~' -exec rm -f {} +
	find . -type f -name '.*~' -exec rm -f {} +
	@echo "$(GREEN)Python cache cleaned.$(NC)"
	poetry install
	poetry run python server.py --streamlit-only

## test: Run all tests
test:
	poetry install --with dev
	poetry run pytest tests/

## lint: Run linters
lint:
	poetry install --with dev
	poetry run mypy --namespace-package -p "langflow_streamlit"

## build: Builds an installable package
build:
	poetry build

publish:
	poetry publish

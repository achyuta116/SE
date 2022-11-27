.PHONY: help
help:
	@echo "---------------COMMANDS-----------------"
	@echo -e "make help\nmake run\nmake server\nmake lint\nmake flake\nmake format\nmake bandit\n"
	@echo "------------------------------------"

.PHONY: run
run: 
	@python main.py

.PHONY: server
server:
	@echo "starting backend server"
	@npx --prefix ./data json-server --watch ./data/database.json --id username

.PHONY: lint
lint:
	@python -m flake8 --version
	@echo -e "Running flake8 on all files...\n"
	@flake8 .

	@python -m pylint --version
	@echo -e "Running pylint on all .py files...\n"
	@pylint --recursive=y "."

.PHONY: flake
flake:
	@python -m flake8 --version
	@echo -e "Running flake8 on all files...\n"
	@flake8 .

.PHONY: format
format:
	@python -m black --version
	@echo -e "Formatting using black..."
	@black .

.PHONY: sort
sort:
	@python -m isort --version
	@echo -e "Formatting using isort..."
	@isort .

.PHONY: bandit
bandit:
	@python -m bandit --version
	@bandit -c bandit.yml -r .

.PHONY: python_version pip_version init_venv activate_venv

python_version: ## Confirm the current python version
	python3 --version

pip_version: ## Confirm the current pip version
	pip3 --version

init_venv: ## Initialize a virtual environment
	python3.15 -m venv .

activate_venv: ## Activate/Start a virtual environment
	source ./bin/activate

.PHONY: brew_install brew_version brew_update brew_upgrade python_install python_version pip_version init_venv activate_venv

## 1: Prerequisites

brew_install: ## Install Homebrew that is the package manager: https://brew.sh/
	/bin/bash -c "$$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

brew_version:
	brew -v

brew_update:
	brew update

brew_upgrade:
	brew upgrade

python_install:
	brew reinstall python@3.15

python_version: ## Confirm the current python version
	python3 --version

pip_version: ## Confirm the current pip version
	pip3 --version

## 2: Setup commands

init_venv: ## Initialize a virtual environment
	python3.15 -m venv .

.PHONY: brew_install brew_v brew_update brew_upgrade py_install py_v pip_v init_venv activate_venv initprj initapp runserver

## 0: Variables

PJNAME?=
APPNAME?=

## 1: Prerequisites

brew_install: ## Install Homebrew that is the package manager: https://brew.sh/
	/bin/bash -c "$$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

brew_v:
	brew -v

brew_update:
	brew update

brew_upgrade:
	brew upgrade

py_install:
	brew reinstall python@3.15

py_v: ## Confirm the current python version
	python3 --version

pip_v: ## Confirm the current pip version
	pip3 --version

## 2: Setup commands

init_venv: ## Initialize a virtual environment
	python3.15 -m venv .

## 3: Init project & app

initprj: ## Create a project
	django-admin startproject ${PJNAME}

initapp: ## Create an app
	cd ./djangotrainingproject && python3 manage.py startapp ${APPNAME}

runserver: ## Run a local server
	cd ./djangotrainingproject && python3 manage.py runserver

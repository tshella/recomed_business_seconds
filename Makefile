VENV ?= venv
PORT ?= 8000
APP_NAME = recomed-api

PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

UVICORN = $(PYTHON) -m uvicorn
PYTEST = $(PYTHON) -m pytest
BLACK = $(PYTHON) -m black
FLAKE8 = $(PYTHON) -m flake8

.PHONY: setup run test lint format docker-build docker-run clean

## Create virtual environment and install dependencies
setup:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt -r requirements-dev.txt

## Run the FastAPI app locally
run:
	$(UVICORN) main:app --reload --port=$(PORT)

## Run unit tests
test:
	$(PYTEST) tests/

## Lint the project with flake8
lint:
	$(FLAKE8) . --exclude=$(VENV),__pycache__

## Format the codebase using black
format:
	$(BLACK) .

## Build Docker image
docker-build:
	docker build -t $(APP_NAME) .

## Run Docker container
docker-run:
	docker run -p $(PORT):8000 $(APP_NAME)

## Clean up Docker containers and images
clean:
	docker rm -f $$(docker ps -aq --filter ancestor=$(APP_NAME)) 2>/dev/null || true
	docker rmi -f $(APP_NAME) 2>/dev/null || true

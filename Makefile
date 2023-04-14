APP_NAME="auto-ml-deploy"
IMAGE_NAME="auto-ml-deploy"
UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Linux)
    DOCKER_USER=$(shell id -u $(USER)):$(shell id -g $(USER))
endif
ifeq ($(UNAME_S),Darwin)
    DOCKER_USER=
endif

local/install:
	pipenv install --dev --skip-lock

local/shell:
	pipenv shell

local/run:
	streamlit run main.py

docker/build:
	CURRENT_UID=${DOCKER_USER} docker-compose build ${APP_NAME}

docker/up/database:
	CURRENT_UID=${DOCKER_USER} docker-compose up -d postgres-db

docker/down/database:
	CURRENT_UID=${DOCKER_USER} docker-compose down postgres-db

docker/up:
	CURRENT_UID=${DOCKER_USER} docker-compose up -d

docker/down:
	CURRENT_UID=${DOCKER_USER} docker-compose down --remove-orphans

docker/run:
	CURRENT_UID=${DOCKER_USER} docker-compose run --service-ports ${APP_NAME} streamlit run main.py
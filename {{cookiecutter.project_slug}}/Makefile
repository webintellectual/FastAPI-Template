include constants.mk

.DEFAULT_GOAL := help
.PHONY: help 

DETACH?=1
ifeq ($(DETACH),1)
    DETACH_FLAG=-d
else
    DETACH_FLAG=
endif

help: ## This prints help text for all the existing commands
	@grep -E '^[0-9a-zA-Z_-]+:.*?## .*$$' Makefile | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%25s:\033[0m %s\n", $$1, $$2}'

check-constants:
	@grep -E '^[^#[:space:]]+=[^#[:space:]]*' constants.mk | while IFS='=' read -r var value; do \
        echo "$$var=$$value"; \
    done

refactor: ## update toml and Dockerfile
	@sed -i '' "s/^name = \".*\"/name = \"$(PROJECT_SLUG)\"/" pyproject.toml
	@sed -i '' "s/^python = \".*\"/python = \"^$(PYTHON_VERSION)\"/" pyproject.toml
	@sed -i '' "s|^WORKDIR .*|WORKDIR /$(PROJECT_SLUG)|" Dockerfile
	@sed -i '' "s|^FROM python:.*|FROM python:$(PYTHON_VERSION)|" Dockerfile
	@sed -i '' "s|^EXPOSE .*|EXPOSE $(CONTAINER_PORT)|" Dockerfile

install: ## Installations of dependencies
	@poetry install

start-server: install 
	@PORT=$(HOST_PORT); \
    if [ -f /.dockerenv ] || grep -q docker /proc/1/cgroup 2>/dev/null; then \
        PORT=$(CONTAINER_PORT); \
    fi; \
    poetry run uvicorn $(PACKAGE_NAME).main:app --reload --host 0.0.0.0 --port $${PORT}

build: install ## Build docker image
	@docker build -t $(IMAGE_NAME) .

deploy: ## Deploy container
	@docker run $(DETACH_FLAG) --rm --name $(CONTAINER_NAME) --label port=$(CONTAINER_PORT) -p $(HOST_PORT):$(CONTAINER_PORT) -v "$$(pwd)":/$(PROJECT_SLUG) $(IMAGE_NAME)

build-deploy: ## Build image and deploy container
	@docker build -t $(IMAGE_NAME) .
	@docker run $(DETACH_FLAG) --rm --name $(CONTAINER_NAME) --label port=$(CONTAINER_PORT) -p $(HOST_PORT):$(CONTAINER_PORT) -v "$$(pwd)":/$(PROJECT_SLUG) $(IMAGE_NAME)

destroy-container: ## Destroy container
	@docker stop $(CONTAINER_NAME)

search-container: ## Search container
	@docker ps -a | grep $(CONTAINER_NAME) || echo "Container not found"
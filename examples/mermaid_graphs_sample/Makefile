PROJECT_DIR = $(shell pwd)
HUGO_BIN = $(shell which hugo)

.PHONY: all run_project check_hugo

all: run_project

run_project: check_hugo
	@echo "Running Project"
	@cd $(PROJECT_DIR) && $(HUGO_BIN) server

check_hugo:
	@if [ -z "$(HUGO_BIN)" ]; then \
		echo "Please install node package manager first" && exit; \
	else \
		echo "Node package manager already installed at $(NPM_BIN)"; \
	fi

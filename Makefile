.DEFAULT_GOAL := help
.PHONY: run build help


build-content: ## Build skycoin docs in ./content/ folder
	rm -rf content/
	mkdir -p content/
	cp -rv _data/* content/
	find content/* -type f -name "*.md" -exec sh -c 'cat _includes/references.md >> "{}" ' \;

build: build-content ## Build docs website
	hugo

run: build-content ## Run docs web site with hugo
	hugo serve -D

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

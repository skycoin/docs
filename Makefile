.DEFAULT_GOAL := help
.PHONY: run build clean help


build: ## Generate static web site
	hugo --buildFuture --config config.toml --destination public -v

clean: ## Remove static web site files
	rm -r public/*

run: ## Run docs web site with hugo
	hugo serve --buildFuture --config config.toml --destination public

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := run
.PHONY: run build


build:       ## Build skycoin docs in ./content/ folder
	rm -rf content/*
	cp -rv _data/* content/
	touch content/.gitkeep
	find content/* -type f -name "*.md" -exec sh -c 'cat _includes/references.md >> "{}" ' \;

run: build   ## Run docs web site with hugo
	hugo serve -D


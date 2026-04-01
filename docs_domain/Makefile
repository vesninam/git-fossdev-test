.PHONY: create-structure test-pytest install-dep install test

create-structure:
	mkdir -p src tests docs
	touch README.md requirements.txt setup.py
	touch src/.gitkeep tests/.gitkeep docs/DOMAIN.md

install-dep:
	pip install -r requirements.txt

install:
	pip install -e .

test-pytest:
	pytest

test: install-dep install test-pytest
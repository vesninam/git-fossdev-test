.PHONY: create-structure install-dep install test-pytest

create-structure:
	mkdir -p src tests docs
	touch src/.gitkeep tests/.gitkeep
	touch docs/DOMAIN.md README.md .gitignore 
	touch setup.py requirements.txt

install-dep:
	pip install -r requirements.txt

install:
	pip install -e .

test-pytest:
	python3 -m pytest

test: install-dep install test-pytest

build-app:
	docker build -t product_service:dev ./

run:
	docker run --rm --name product-service -p 8001:8000 product_service:dev




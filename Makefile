install:
	 poetry install

test:
	poetry run pytest -s --disable-warnings

build:
	rm -rf ./dist
	poetry export -f requirements.txt > requirements.txt
	poetry build

publish: build
	poetry publish

config:
	poetry config virtualenvs.create false --local

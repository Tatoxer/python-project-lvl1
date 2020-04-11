install:
	poetry install

lint:
	poetry run flake8 brain_games

test-coverage:
	npm test -- --coverage

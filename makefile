install:
	poetry install

without-build:
	python3 -m pip install .

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

build-install:
	poetry build
	python3 -m pip install --user --force-reinstall dist/*.whl

to-greet:
	poetry run to-greet

play:
	to-greet
	brain-calc

brain-even:
	poetry run brain-even

lint:
	poetry run flake8 brain_games

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

brain-prime:
	poetry run brain-prime

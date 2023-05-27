install:
	poetry install

without-build:
	python3 -m pip install .

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

build:
	poetry build
	make package-install
	poetry update

publish:
	poetry publish --dry-run

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

play:
	poetry run play

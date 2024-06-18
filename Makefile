format:
	yapf -r -i drive
	yapf -r -i tests
	yapf -i main.py

type-analyze:
	pytype --protocols drive tests main.py

update: format
	pip install -e .

test-all: type-analyze test

test: update
	coverage run --omit=./tests/* -m unittest discover -s tests -v && coverage report -m --include=./*

clean:
	rm -rf .pytpe
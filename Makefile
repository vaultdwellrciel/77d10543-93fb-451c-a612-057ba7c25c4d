lint: dev_dependencies
	flake8 .

dev_dependencies:
	pip install --upgrade --requirement requirements.dev.txt

dependencies:
	pip install --upgrade --requirement requirements.txt

test: dependencies lint
	python setup.py check
	check-manifest
	python -m unittest discover -v -t . -s test

coverage:
	coverage run -m unittest discover -t . -s test 2> /dev/null
	coverage report -m

.PHONY: test lint dependencies dist dev_dependencies

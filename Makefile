project := quantcast_assignment

pytest := coverage run -m pytest cookie_log_parser/tests --junitxml=test-results/junit.xml

clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -f `find . -type f -name '@*' `
	rm -f `find . -type f -name '#*#' `
	rm -f `find . -type f -name '*.orig' `
	rm -f `find . -type f -name '*.rej' `
	rm -f .coverage
	rm -rf coverage
	rm -rf build
	rm -rf htmlcov
	rm -rf dist

flake:
	flake8 cookie_log_parser

black:
	python -m black cookie_log_parser

test:
	$(pytest)

install-dev:
	pip install -r requirements-dev.txt

.PHONY: flake black clean test run

coverage-report:
	coverage html -d htmlcov

serve-report: coverage-report
	python -m http.server --directory ./htmlcov/ $(port)

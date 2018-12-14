export PYTHONPATH=${CURDIR}

.PHONY: all test coverage flake8 clean

all: test coverage flake8

test:
	py.test

coverage:
	coverage run --source jutge -m py.test
	coverage report

# we ignore the "E501 line too long" diagnostics
flake8:
	flake8  --ignore=E501 --exclude test/timing/

clean:
	rm -rf .cache MANIFEST dist .coverage htmlcov */*,cover */__pycache__ *~ */*~ */*.pyc


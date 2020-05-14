export PYTHONPATH=${CURDIR}

.PHONY: all coverage flake8 clean

all: coverage flake8

coverage:
	coverage run --source easyinput -m test.py
	coverage report

# we ignore the "E501 line too long" and "F403 'import *'" diagnostics
flake8:
	flake8 --ignore=E501,F403,F405 easyinput/

clean:
	rm -rf .cache MANIFEST dist .coverage htmlcov */*,cover */__pycache__ *~ */*~ */*.pyc


export PYTHONPATH=${CURDIR}

.PHONY: all test coverage clean

all:
	@echo "Targets: test coverage clean"

test:
	py.test

coverage:
	coverage run --source jutge -m py.test
	coverage report

clean:
	rm -rf .cache MANIFEST dist .coverage htmlcov */*,cover */__pycache__ *~ */*~ */*.pyc


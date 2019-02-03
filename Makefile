export PYTHONPATH=${CURDIR}

.PHONY: all coverage flake8 clean

all: coverage flake8

coverage:
	coverage run --source jutge -m py.test
	coverage report

# we ignore the "E501 line too long" diagnostics
flake8:
	cd jutge
	flake8  --ignore=E501,F403
	cd ..

clean:
	rm -rf .cache MANIFEST dist .coverage htmlcov */*,cover */__pycache__ *~ */*~ */*.pyc


export PYTHONPATH=${CURDIR}

.PHONY: test all

all:
	@echo "Targets: test"

test:
	pytest

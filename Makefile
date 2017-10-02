.PHONY: help install test molecule all clean

help:
	@echo "Available targets are:"
	@echo "- install  - install all dependencies"
	@echo "- molecule - run molecule tests"
	@echo "- test     - run all tests"
	@echo "- clean    - clean up the workspace"

install:
	pip install -r requirements.txt

molecule:
	@echo
	@echo "Currently, no tests because of https://github.com/ansible/ansible/issues/27747"
	@echo

test: molecule

all: install molecule

clean:
	rm -rf molecule/*/.molecule
	rm -rf molecule/*/tests/__pycache__
	find . -name \*.pyc -delete

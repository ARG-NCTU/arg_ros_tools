.ONESHELL:
SHELL := /bin/bash
SRC = $(wildcard ./*.ipynb)

all: arg_ros_tools docs

clean:
	nbdev_clean

arg_ros_tools: $(SRC)
	nbdev_export
	touch arg_ros_tools

sync:
	nbdev_update_lib

docs_serve: docs
	cd docs && bundle exec jekyll serve

docs: $(SRC)
	nbdev_docs
	touch docs

test:
	nbdev_test_nbs

release: pypi conda_release
	nbdev_bump_version

conda_release:
	fastrelease_conda_package

pypi: dist
	#twine upload --repository pypi dist/*
	twine upload --skip-existing --repository pypi dist/*

dist: clean
	python3 setup.py sdist bdist_wheel

clean:
	rm -rf dist

# Makefile for contributor guide
html: build

build: Makefile source/* source/images/* source/_static/css/* source/meetings/*
	mkdir -p build
	touch build
	#tox
	sphinx-build -b html source build/html

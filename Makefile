.PHONY: init dev test clean

all:

init:
	pip install -r requirements.txt

dev:
	pip install -e .

coverage: dev
	python report_coverage.py

test: dev
	python tests/test_web.py

web: dev
	python modules/web/get_site.py

clean:
	pip uninstall mypkg


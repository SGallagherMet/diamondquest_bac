none: help

help:
	@echo "DiamondQuest: A math mining adventure."
	@echo
	@echo "run			Run DiamondQuest."
	@echo "test			Run pytests for DiamondQuest."
	@echo "tidy			Tidy up cruft (pyc, pycache, eggs)."
	@echo
	@echo "venv			Build the venv based on requirements.txt"
	@echo "clean		Delete the venv"

clean:
	rm -r venv

venv:
	python3.7 -m venv venv
	venv/bin/pip install --upgrade pip
	venv/bin/pip install -r requirements.txt -r requirements_dev.txt
	
run: venv
	cd src && ../venv/bin/python3 -m diamondquest

format: venv
	cd src && ../venv/bin/black -l 80 diamondquest

test: venv
	cd src && ../venv/bin/python3 -m pytest diamondquest
	
tidy: venv
	venv/bin/python3 -m pycleanup --egg --pyc --cache

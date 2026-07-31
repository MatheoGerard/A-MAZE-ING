VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

$(VENV):
	python3 -m venv $(VENV)

install: $(VENV)
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) -m a_maze_ing config.txt

debug:
	$(PYTHON) -m pdb a_maze_ing.py config.txt


clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +

lint:
	-$(PYTHON) -m flake8 . --exclude=.venv
	$(PYTHON) -m mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	-$(PYTHON) -m flake8 . --exclude=.venv
	$(PYTHON) -m mypy --strict .



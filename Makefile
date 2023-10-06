.PHONY: lint
lint: lint-mypy

.PHONY: lint-mypy
lint-mypy:
	@mypy esbill

.PHONY: test
test:
	python -m unittest tests/*/*.py

.PHONY: lint
lint: lint-mypy

.PHONY: lint-mypy
lint-mypy:
	@mypy esbill

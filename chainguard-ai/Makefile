.PHONY: demo backend frontend install install-backend install-frontend data run-pipeline test test-backend test-frontend build lint typecheck verify clean help

PYTHON ?= python
PIP ?= $(PYTHON) -m pip
HOST ?= 127.0.0.1
BACKEND_PORT ?= 8000
FRONTEND_PORT ?= 5173

help:
	@echo "ChainGuard AI targets:"
	@echo "  make install        - install backend (venv) + frontend deps"
	@echo "  make data           - generate deterministic demo dataset"
	@echo "  make run-pipeline   - run full offline analysis pipeline (headless)"
	@echo "  make demo           - ONE-COMMAND DEMO: data -> pipeline -> backend -> frontend"
	@echo "  make backend        - start backend only"
	@echo "  make frontend       - start frontend dev server only"
	@echo "  make test           - backend + frontend tests"
	@echo "  make build          - frontend production build"
	@echo "  make verify         - installation verification"

install: install-backend install-frontend

install-backend:
	$(PYTHON) -m venv .venv
	.venv/Scripts/python -m pip install -r requirements.txt || ( source .venv/bin/activate && pip install -r requirements.txt )

install-frontend:
	npm --prefix frontend install

data:
	$(PYTHON) scripts/generate_demo_data.py

run-pipeline:
	$(PYTHON) scripts/run_pipeline.py

demo:
	$(PYTHON) scripts/run_demo.py

backend:
	$(PYTHON) -m uvicorn backend.app.main:app --host $(HOST) --port $(BACKEND_PORT)

frontend:
	npm --prefix frontend run dev -- --port $(FRONTEND_PORT) --strictPort

test: test-backend test-frontend

test-backend:
	$(PYTHON) -m pytest backend/tests -v

test-frontend:
	npm --prefix frontend test -- --run

build:
	npm --prefix frontend run build

lint:
	$(PYTHON) -m ruff check backend scripts || true

typecheck:
	npm --prefix frontend run typecheck

verify:
	$(PYTHON) scripts/verify_installation.py

clean:
	rm -rf backend/storage/* data/uploads/* data/generated/* ml/artifacts/*.pkl 2>/dev/null || true

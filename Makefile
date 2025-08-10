# LangChain Documentation Helper - Makefile
# Provides convenient commands for development and deployment

.PHONY: help install install-dev setup run ingest test clean lint format

# Default target
help:
	@echo "LangChain Documentation Helper - Available Commands:"
	@echo ""
	@echo "Setup Commands:"
	@echo "  install     - Install production dependencies"
	@echo "  install-dev - Install development dependencies"
	@echo "  setup       - Initial project setup (install + env template)"
	@echo ""
	@echo "Runtime Commands:"
	@echo "  run         - Start the Streamlit web application"
	@echo "  ingest      - Run documentation ingestion process"
	@echo ""
	@echo "Development Commands:"
	@echo "  test        - Run tests (when available)"
	@echo "  lint        - Run code linting"
	@echo "  format      - Format code with black and isort"
	@echo "  clean       - Clean up temporary files"
	@echo ""

# Installation commands
install:
	@echo "Installing production dependencies..."
	pip install -r requirements.txt

install-dev:
	@echo "Installing development dependencies..."
	pipenv install --dev

# Setup command for new users
setup: install-dev
	@echo "Setting up LangChain Documentation Helper..."
	@if [ ! -f .env ]; then \
		cp .env.example .env; \
		echo "Created .env file from template"; \
		echo "Please edit .env with your API keys before running"; \
	else \
		echo ".env file already exists"; \
	fi
	@echo "Setup complete! Edit .env with your API keys, then run 'make run'"

# Runtime commands
run:
	@echo "Starting LangChain Documentation Helper..."
	streamlit run main.py

ingest:
	@echo "Starting documentation ingestion..."
	python ingestion.py

# Development commands
test:
	@echo "Running tests..."
	# Add test command when tests are available
	@echo "No tests configured yet"

lint:
	@echo "Running code linting..."
	@echo "Checking with flake8..."
	-flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	@echo "Checking with pylint..."
	-pylint **/*.py

format:
	@echo "Formatting code..."
	black .
	isort .

clean:
	@echo "Cleaning up temporary files..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type f -name ".DS_Store" -delete

# Deployment helpers (for future use)
docker-build:
	@echo "Building Docker image..."
	docker build -t langchain-doc-helper .

docker-run:
	@echo "Running Docker container..."
	docker run -p 8501:8501 langchain-doc-helper

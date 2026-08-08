# DevOps Skills with GitHub

This repository is a simple starter project for practicing DevOps-style workflows with GitHub, Python, and common quality tools.

## Overview

The project includes:
- A Python dependency list in requirements.txt
- A Makefile with common development commands
- Basic tooling for testing, formatting, linting, and refactoring

## Prerequisites

- Python 3.8+
- pip

## Getting Started

Install the required dependencies:

```bash
make install
```

Or manually:

```bash
pip install -r requirements.txt
```

## Available Commands

The Makefile provides these helper targets:

```bash
make test        # Run the test suite
make format      # Format code with Black and isort
make limit       # Check linting and line length constraints
make refactor    # Run automated cleanup tools
```

## Project Notes

This repository is intentionally lightweight and is meant to be used as a learning or demo project for:
- GitHub-based workflows
- Python environment setup
- Automated quality checks
- Basic DevOps automation practices

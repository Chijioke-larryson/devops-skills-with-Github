# DevOps Skills with GitHub

This repository is a lightweight starter project for practicing DevOps workflows with GitHub, Python, and common automation tools.

## What’s in this project

- A simple Python script in [hello.py](hello.py)
- A dependency list in [requirements.txt](requirements.txt)
- A [Makefile](Makefile) with useful development commands
- Basic tooling for testing, formatting, linting, and cleanup

## Prerequisites

- Python 3.8 or newer
- pip

## Getting started

Install dependencies:

```bash
make install
```

You can also install them directly:

```bash
pip install -r requirements.txt
```

Run the example script:

```bash
python hello.py
```

## Useful commands

The Makefile includes the following targets:

```bash
make test        # Run the test suite
make format      # Format code with Black and isort
make limit       # Check linting and line length rules
make refactor    # Run automated cleanup tools
```

## Purpose

This repository is intended as a simple learning environment for:
- GitHub-based collaboration
- Python project setup
- Automated quality checks
- Basic DevOps practices

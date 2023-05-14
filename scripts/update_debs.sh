#!/usr/bin/env bash

# Assumes venv is activated.

# Turn on bash strict mode.
set -euxo pipefail

# Delete dep files.
rm -rf requirements-*.txt

# Install dev dependencies.
pip install pip-tools

# Update the deps.
pip-compile /root/work/abantether/requirements.in -o /root/work/abantether/requirements.txt 


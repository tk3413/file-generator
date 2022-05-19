#!/bin/bash

echo "sorting imports"
isort .

echo "formatting code"
black src/ && black e2e/ && black test/

echo "applying linter"
pylint src/ && pylint e2e/ && pylint test/

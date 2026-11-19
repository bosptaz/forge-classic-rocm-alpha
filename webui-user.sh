#!/usr/bin/env bash

# ROCm-only configuration: forces the environment to the project's .venv
# and enables the uv installer hook.
export VENV_DIR="$(cd "$(dirname "$0")" && pwd)/.venv"
export PYTHON=python3.13
export TORCH_COMMAND="pip install torch==2.12.1 torchvision==0.27.1 --index-url https://download.pytorch.org/whl/rocm7.1"

export COMMANDLINE_ARGS="--uv --api"

# --skip-python-version-check --skip-torch-cuda-test --skip-version-check --skip-prepare-environment --skip-install

exec "$(dirname "$0")/webui.sh" $COMMANDLINE_ARGS

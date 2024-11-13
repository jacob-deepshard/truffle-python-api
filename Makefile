.PHONY: protos install dev test help init

# Directory paths
MAKEFILE_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
PROTO_BASE_DIR = $(MAKEFILE_DIR)/truffleos-protobuf
PROTO_OUTPUT_DIR = $(MAKEFILE_DIR)/truffle_cli/protos

# OS-specific commands
ifeq ($(OS),Windows_NT)
	MKDIR_P = mkdir
	RMDIR = rmdir /s /q
else
	MKDIR_P = mkdir -p
	RMDIR = rm -rf
endif

# Initialize git submodules
init:
	git submodule update --init --recursive

all: init protos

protos:
	make -f $(PROTO_BASE_DIR)/Makefile python OVERRIDE_OUT_DIR=$(PROTO_OUTPUT_DIR)

# Install dependencies
install: protos
	poetry install

# Run development environment
dev: install
	poetry shell

# Run tests
test: install
	poetry run pytest

# Debug target
debug: install
	poetry run python -m debugpy --listen 5678 --wait-for-client -m truffle_cli

# Help target
help:
	@echo "Available targets:"
	@echo "  init          - Initialize git submodules"
	@echo "  protos        - Update Python protobuf files from truffleos-protobuf into truffle_cli/protos"
	@echo "  install       - Install project dependencies"
	@echo "  dev          - Start development shell"
	@echo "  test         - Run tests"
	@echo "  debug        - Start CLI in debug mode (listening on port 5678)"
	@echo "  help         - Show this help message" 
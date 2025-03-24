# PA053 Homework 1

## Prerequisites

- `uv`

## Usage

```sh
uv run main.py
```

## GRPC generation

```sh
uv run -m grpc_tools.protoc .\homework.proto --python_out=. -I . --pyi_out=. --grpc_python_out="."
```

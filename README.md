# NovaAI

NovaAI is a Python package for running the NovaV1 AI model locally.

## Features

* Automatically downloads the NovaV1 model when needed
* Stores the model locally
* Runs the model locally on the user's computer
* Simple Python interface

## Installation

Clone the repository:

```bash
git clone https://github.com/PSAkillerPSA/NovaAI.git
cd NovaAI
```

Install NovaAI:

```bash
pip install .
```

## Usage

```python
from novaai import get_model_path

model_path = get_model_path()

print(f"Model path: {model_path}")
```

On the first run, NovaAI automatically downloads `novaV1.gguf`.

The model is then stored locally so it does not need to be downloaded again.

## Model

NovaAI uses the NovaV1 model in GGUF format.

The model is downloaded automatically when it is needed.

## Project Structure

```text
NovaAI/
├── src/
│   └── novaai/
│       ├── __init__.py
│       └── model.py
│
├── README.md
├── pyproject.toml
└── LICENSE
```

## Status

NovaAI is currently under development.

## License

NovaAI is placed under the MIT license. See license.txt for more details.

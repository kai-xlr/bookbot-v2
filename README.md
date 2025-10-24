# BookBot

A Python application for book-related tasks.

## Installation

### Development Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd bookbot
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the package in editable mode with development dependencies:
```bash
pip install -e ".[dev]"
```

## Usage

Run the application:
```bash
bookbot
```

Or run directly with Python:
```bash
python -m bookbot.main
```

## Development

### Running Tests

Run all tests with coverage:
```bash
pytest
```

Run specific test file:
```bash
pytest tests/test_main.py
```

Run tests without coverage:
```bash
pytest --no-cov
```

### Linting and Formatting

Check code with Ruff:
```bash
ruff check .
```

Format code with Ruff:
```bash
ruff format .
```

Fix auto-fixable issues:
```bash
ruff check --fix .
```

### Type Checking

Run type checking with mypy:
```bash
mypy src
```

## Project Structure

```
bookbot/
├── src/
│   └── bookbot/          # Main package
│       ├── __init__.py
│       └── main.py       # Application entry point
├── tests/                # Test suite
│   ├── __init__.py
│   └── test_main.py
├── docs/                 # Documentation
├── pyproject.toml        # Project configuration and dependencies
├── README.md
└── .gitignore
```

## License

TBD

BookBot is my first [Boot.dev](https://www.boot.dev) project!

# Agent Guidelines for VirtualJarvis

## Build/Lint/Test Commands
- **Install**: `pip install -r requirements.txt`
- **Run app**: `python main.py`
- **Type check**: `python -m mypy *.py`
- **Syntax check**: `python -m py_compile *.py`
- **Test streaming**: `python test_pyaudio.py`
- **Test single module**: `python -m pytest module_name.py -v` (if pytest available)

## Code Style Guidelines

### Imports & Naming
- Group: stdlib → third-party → local imports (blank line between groups)
- Functions: snake_case (`recordAudio`, `gemini_chat`)
- Classes: PascalCase (`Jarvis`)
- Variables: snake_case (`api_key`, `transcribed_text`)

### Formatting & Types
- 4-space indentation, ~80-100 char lines
- Type hints: Required for function parameters/returns (`def modelAnswer(self, response: str) -> None`)
- Error handling: try/except with specific exceptions and meaningful messages
- Environment vars: `os.getenv()` for API keys, never hardcode secrets

### Best Practices
- `if __name__ == "__main__":` guards for executable scripts
- Single responsibility functions/methods
- Descriptive variable names, avoid abbreviations
- Security: Never commit API keys or secrets
- Threading: Use producer-consumer pattern with queues for audio streaming

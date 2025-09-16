# Agent Guidelines for VirtualJarvis

## Build/Lint/Test Commands
- **Install**: `pip install -r requirements.txt`
- **Run app**: `python main.py`
- **Type check**: `python -m mypy *.py`
- **Syntax check**: `python -m py_compile *.py`
- **Test single module**: `python -m module_name`

## Code Style Guidelines

### Imports & Naming
- Group: stdlib → third-party → local imports
- Functions: snake_case (`recordAudio`, `gemini_chat`)
- Classes: PascalCase (`Jarvis`)
- Variables: snake_case (`api_key`, `transcribed_text`)

### Formatting & Types
- 4-space indentation, ~80-100 char lines
- Type hints: `def modelAnswer(self, response: str)`
- Error handling: try/except with meaningful messages
- Environment vars: `os.getenv()` for API keys

### Best Practices
- `if __name__ == "__main__":` guards
- Single responsibility functions
- Descriptive variable names
- Security: Never commit API keys

## Streaming Audio
- **Test streaming**: `uv run python test_pyaudio.py`
- **Enable streaming**: `STREAMING_MODE=true python main.py`
- Uses producer-consumer pattern with threads/queues
- Dependencies: pyaudio, kokoro, google-genai

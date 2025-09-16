# Agent Guidelines for VirtualJarvis

## Build/Lint/Test Commands
- **Install dependencies**: `pip install -r requirements.txt`
- **Run main application**: `python main.py`
- **Type checking**: `python -m mypy *.py` (install mypy first: `pip install mypy`)
- **Basic syntax check**: `python -m py_compile *.py`
- **No test framework configured** - run individual modules with `python -m module_name`

## Code Style Guidelines

### Imports
- Use relative imports for internal modules: `from gemini_model import gemini_chat`
- Group imports: standard library first, then third-party, then local
- One import per line

### Naming Conventions
- **Functions**: snake_case (`recordAudio`, `gemini_chat`)
- **Classes**: PascalCase (`Jarvis`)
- **Variables**: snake_case (`api_key`, `transcribed_text`)
- **Constants**: UPPER_CASE (not observed in codebase)

### Formatting
- 4 spaces for indentation (Python standard)
- Line length: ~80-100 characters
- Blank lines between functions and classes

### Types & Error Handling
- Use type hints where beneficial: `def modelAnswer(self, input_content: str)`
- Handle exceptions with try/except blocks
- Use `os.getenv()` for environment variables
- Return meaningful error messages
- **Current issues**: Fix type errors in main.py (tuple operations, None handling) and stt.py (method calls, parameter types)

### Best Practices
- Use `if __name__ == "__main__":` guards
- Keep functions focused on single responsibilities
- Use descriptive variable names
- Add minimal but clear comments for complex logic

### Security
- Store API keys in environment variables (GEMINI_API_KEY)
- Never commit sensitive data to repository

## Streaming Audio Implementation

### Overview
The app supports concurrent streaming audio to reduce AI response wait times. AI text generation, TTS processing (Kokoro), and audio playback (PyAudio) run in parallel using threads and queues. Streaming is enabled by default in `test_pyaudio.py`; toggle via `STREAMING_MODE` env var in full app.

### Key Components
- **Producer-Consumer Pattern**: AI yields text chunks → buffered to sentences → Kokoro generates audio → PyAudio streams in 1024-sample chunks.
- **Concurrency**: Threads overlap processes; no disk I/O for real-time playback.
- **Dependencies**: Requires `pyaudio`, `kokoro`, `google-genai`. Install via `uv` or pip.

### Testing Commands
- **Standalone Streaming Test**: `uv run python test_pyaudio.py` – Tests full pipeline with hardcoded input ("Tell me a short story about AI."). Expects audio playback (if device available); monitors latency.
- **Integrated App Test**: `uv run STREAMING_MODE=true TEST_MODE=true python main.py` – Runs full app with streaming; uses env vars for modes.
- **Troubleshooting**: Check `GEMINI_API_KEY` env var. In headless env, audio may not play (ALSA warnings expected). Measure time for concurrency validation.

### Benefits
- Eliminates long waits by overlapping AI/TTS/playback.
- Sentence-level chunking maintains TTS quality.
- Default streaming reduces perceived latency.

### Notes
- Built in `test_pyaudio.py` for isolation; merge to `main.py` for production.
- No IPython dependencies; CLI-compatible.
- If issues, verify PyAudio installation and audio device.

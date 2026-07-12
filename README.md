# Voice Assistant

Voice Assistant is an offline desktop assistant written in Python. It recognizes voice commands, processes them through an intent-based routing system, executes the corresponding action, and responds using text-to-speech.

## Features

- Offline speech recognition
- Offline text-to-speech
- User authentication
- Notes management
- Timers
- Weather forecast
- Calculator
- Browser search (Google, YouTube, Wikipedia)
- Date and time
- User logs
- Automated tests

## Technologies

- Python 3.12
- PostgreSQL
- Psycopg
- Vosk
- PyAudio
- pyttsx3
- CustomTkinter
- Requests
- Pytest

## Architecture

The application follows a modular architecture:

- `Recorder` – records microphone audio.
- `SpeechToText` – converts speech to text.
- `IntentRecognizer` – detects the user's intent.
- `Router` – routes requests to the appropriate skill.
- `Skills` – implement assistant functionality.
- `AuthManager` – handles user authentication.
- `DatabaseManager` – manages PostgreSQL operations.
- `Logger` – stores command history.
- `TextToSpeech` – generates voice responses.

## Installation

```bash
git clone https://github.com/your_username/VoiceAssistant.git
cd VoiceAssistant

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
python main.py
```

## Testing

```bash
pytest
```

## License

MIT License

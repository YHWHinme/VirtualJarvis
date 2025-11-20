# This script integrates Speech-to-Text (STT), a Gemini language model, and Text-to-Speech (TTS)
# to create an interactive voice assistant.


# from gemini_model import gemini_chat
from ollama_model import ollama_chat, ollama_chat_stream
from stt import recordAudio
from tts import speakText, speakText_chunk
import os


def is_sentence_end(text):
    if not text.strip():
        return False
    return text.strip()[-1] in ".!?"


class Jarvis:
    def __init__(self):
        self.stt_data = ""
        self.listening = False
        self.stt = self.transcribeLoop()

        # Starts the sequence
        self.Greet()

    # Greets and turns on listening state
    def Greet(self):
        print("Starting engine")
        self.listening = True
        self.Main()

    def transcribeLoop(self):
        while self.listening:
            recorded_data = recordAudio()
            print(f"Recorded data: {recorded_data}")
            print("\n\nChecking for data")

            if recorded_data and recorded_data not in ["An error occured", None]:
                self.stt_data = recorded_data  # Overwrite with new string
                self.toggleListening()
                break
            else:
                print("No valid data, trying again")

    # NOTE: Thinking functions
    def think(self):
        model_input = self.stt_data
        response = (
            ollama_chat(model_input)["message"]["content"] or "Sorry, I couldn't generate a response."
        )
        return response

        # TODO:  Colagalate these thinkin functions into one

    def remoteThink_ollama_stream(self, model: str):
        model_input = self.stt_data
        for chunk in ollama_chat_stream(model_input):
            yield chunk

    def modelAnswer(self, response: str):
        speakText(response)

    def modelAnswer_stream(self, chunk_generator):
        buffer = ""
        for chunk in chunk_generator:
            buffer += chunk
            if is_sentence_end(buffer):
                speakText_chunk(buffer)
                buffer = ""
        if buffer:
            speakText_chunk(buffer)

    def Main(self):
        streaming_mode = os.getenv("STREAMING_MODE", "false").lower() == "true"
        while True:
            self.transcribeLoop()
            if streaming_mode:
                chunk_gen = self.remoteThink_ollama_stream("gemma3:4b-it-qat")
                self.modelAnswer_stream(chunk_gen)
            else:
                response = self.think()
                self.modelAnswer(response)
            self.listening = True

    # NOTE: Toggles listening state
    def toggleListening(self):
        self.listening = not self.listening


if __name__ == "__main__":
    jarvis = Jarvis()

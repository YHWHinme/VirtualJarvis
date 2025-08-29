# This script integrates Speech-to-Text (STT), a Gemini language model, and Text-to-Speech (TTS)
# to create an interactive voice assistant.

from gemini_model import gemini_chat
from stt import recordAudio
from tts import speakText


# TODO: Create a class that contains a listening state
class Jarvis:
    def __init__(self):
        self.stt_data = []
        self.listening = False
        self.greeting = self.Greet()
        self.stt = self.transcribeLoop()
    

    # Greets and turns on listening state
    def Greet(self):
        print("Starting engine")
        self.listening = True

    def transcribeLoop(self):
        while self.listening:
            recorded_data = recordAudio()
            self.stt_data.append(recorded_data)
            print("\n\nChecking for data")

            if len(self.stt_data) == 0:
                print("Data is empty, trying again")
                # TODO: Write to an empty list
            else:
                self.toggleListening()


                    
    # Toggles listening state
    def toggleListening(self):
        self.listening = not self.listening

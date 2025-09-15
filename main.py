# This script integrates Speech-to-Text (STT), a Gemini language model, and Text-to-Speech (TTS)
# to create an interactive voice assistant.


from gemini_model import gemini_chat
from stt import recordAudio
from tts import speakText


class Jarvis:


    def __init__(self):
        self.stt_data = ""
        self.listening = False
        self.stt = self.transcribeLoop()

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
    def think(self):
        model_input = self.stt_data
        response = gemini_chat(model_input).text or "Sorry, I couldn't generate a response."
        return response

    def modelAnswer(self, response: str):
        speakText(response)

    def Main(self):
        while True:
            self.transcribeLoop()
            response = self.think()
            self.modelAnswer(response)
            self.listening = True




    # Toggles listening state
    def toggleListening(self):
        self.listening = not self.listening

if __name__ == "__main__":
    jarvis = Jarvis()

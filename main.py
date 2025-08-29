# This script integrates Speech-to-Text (STT), a Gemini language model, and Text-to-Speech (TTS)
# to create an interactive voice assistant.


from gemini_model import gemini_chat
from stt import recordAudio
from tts import speakText


# TODO: Create a class that contains a listening state
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
            self.stt_data += recorded_data
            print(self.stt_data)
            print("\n\nChecking for data")

            if not self.stt_data:
                print("Data is empty, trying again")
            else:
                self.toggleListening()
                break
    def think(self):
        model_input = self.stt_data
        response = gemini_chat(model_input).text
        return response

    def modelAnswer(self, input_content: str):
        input_content = self.think()
        speakText(input_content)

    def Main(self):
        while True:
            self.transcribeLoop()
            response = self.think()
            self.modelAnswer(response)




    # Toggles listening state
    def toggleListening(self):
        self.listening = not self.listening

if __name__ == "__main__":
    jarvis = Jarvis()

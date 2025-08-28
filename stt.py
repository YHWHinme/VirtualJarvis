

import speech_recognition as sr


def recordAudio():
    listening = True
    recorder =  sr.Recognizer()
    while listening:
        try:
            with sr.Microphone() as source2:
                recorder.adjust_for_ambient_noise(source2, duration=0.2)
                
                #listens to the user's audio input
                print("\n\nListening...")
                audio2 = recorder.listen(source2)

                # Transcribed text
                transcribed_text = recorder.recognize_google(audio2)
                print("Processing...")
                listening = False
                return transcribed_text
        except sr.RequestError as e:
            print(f"Request Error {e}")
            return "An error occured"

        except sr.UnknownValueError:
            print("Unknown error occured")


def saveDisk():
    with open("recordedTranscribe.txt", "w") as f:
        writable = recordAudio()
        f.write(writable)

if __name__ == "__main__":
    saveDisk()



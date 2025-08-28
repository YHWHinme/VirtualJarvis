# This script integrates Speech-to-Text (STT), a Gemini language model, and Text-to-Speech (TTS)
# to create an interactive voice assistant.

from gemini_model import gemini_chat
from stt import recordAudio
from tts import speakText

# TODO: Encapsulate the stt function in main for continous trial


def main_func():
   # Record audio input from the user using the Speech-to-Text (STT) module.

   stt_input = recordAudio(gemini= True)
   if gemini:
        # Send the transcribed text to the Gemini model for a response.
        print("Loading Gemini")
        model_content = gemini_chat(stt_input).text
   else:
        # Send the transcribed text to the ollama model for a response.
        print("Loading ollama")
        model_content = ollama_chat(stt_input)["message"]["content"]

   # Clean the model's response by removing markdown characters.
   stripped_content = model_content.replace('*', '').replace('#', '').replace('-', '')
    model_answer = (stripped_content)

   # Save the cleaned model response to a text file.
   with open('model_answer.txt', 'w') as f:
       f.write(model_answer)

   # Convert the model's response to speech using the Text-to-Speech (TTS) module.
   speakText(stripped_content)


if __name__ == "__main__":
    main_func()

import sys
from ollama_model import ollama_chat
from gemini_model import gemini_chat
from tts import speakText

def main_func(input_content):
    model_content = ollama_chat(input_content)["message"]["content"]
    # model_content = gemini_chat(input_content)
    model_answer = (model_content)
    print(model_answer)

    speakText(model_content)


if __name__ == "__main__":
    user_input = sys.argv[1]
    main_func(user_input)

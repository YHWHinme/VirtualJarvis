#imports
import os
import sys

from google import genai

#Loading envs
api_key = os.getenv("GEMINI_API_KEY")

def gemini_chat(input, model= "gemini-2.5-flash"):
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model= model,
        contents = input,
    )
    return response

def gemini_chat_stream(input, model="gemini-2.5-flash"):
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content_stream(
        model=model,
        contents=input,
    )
    for chunk in response:
        if chunk.text:
            yield chunk.text

if __name__ == "__main__":
    user_input = sys.argv[1]
    for _, chunk in enumerate(gemini_chat_stream(user_input)):
        print(chunk)

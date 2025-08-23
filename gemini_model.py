#imports
from google import genai
import sys
import os

#Loading envs
api_key = os.getenv("GEMINI_API_KEY")

def gemini_chat(input, model= "gemini-2.5-flash"):
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model= model,
        contents = input,
    )
    return response

if __name__ == "__main__":
    user_input = sys.argv[1]
    print(gemini_chat(user_input).text)

from ollama import chat
from ollama import ChatResponse
import sys

def ollama_chat(content):

    # TODO: Also make a print statement every 10 seconds to let you know he's doing something
    response: ChatResponse = chat(model='gemma3:4b-it-qat', messages=[
        {
            'role': 'user',
            'content': content,
        },
    ])
    return response

def ollama_chat_stream(content):
    response = chat(model='gemma3:4b-it-qat', messages=[
        {
            'role': 'user',
            'content': content,
        },
    ], stream=True)
    for chunk in response:
        if chunk['message']['content']:
            yield chunk['message']['content']

# or access fields directly from the response object

if __name__ == "__main__":
    user_input = sys.argv[1]
    print(ollama_chat(user_input)["message"]["content"])

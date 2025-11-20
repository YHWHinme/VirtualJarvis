from ollama import ChatResponse
from ollama import Client 
import sys


client = Client(host="http://172.16.5.39:3000")

def ollama_chat(content, client=client ):

    client = Client(host="http://172.16.5.39:3000")

    # TODO: Also make a print statement every 10 seconds to let you know he's doing something
    response: ChatResponse = client.chat(model='gemma3:4b', messages=[
        {
            'role': 'user',
            'content': content,
        },
    ])
    return response

def ollama_chat_stream(content, client=client):
    response = client.chat(model='gemma3:4b', messages=[
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

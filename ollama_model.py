from ollama import chat
from ollama import ChatResponse
import sys

def ollama_chat(content):
    response: ChatResponse = chat(model='gemma3:1b-it-qat', messages=[
        {
            'role': 'user',
            'content': content,
        },
    ])
    return response['message']['content']
# or access fields directly from the response object

if __name__ == "__main__":
    user_input = sys.argv[1]
    print(ollama_chat(user_input))

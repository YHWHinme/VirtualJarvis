# TODO: Create another instance of llm inside another file called formatter in order to format the file

import sys

from ollama_model import ollama_chat


def format_file(input_content: str, switch= True):
    def formatter(unformated_content):
        # TODO: Format the file here
        example = """
        \n\nIf the file has any occurance of anything similar to this

            ```bash
                some command here
            ```
            Ensure this text here is embellished and put it in it's own line
        """
        added_prompt = f"Format this file according to the following example {example}"
        llm_prompt = unformated_content + added_prompt
        llm_content = ollama_chat(llm_prompt)
        return llm_content
    if switch:
        with open(input_content, "r") as f:
            file_content = f.read()
            file_formatted = formatter(file_content)
            return file_formatted
    else:
        content_formatted = formatter(input_content)
        return content_formatted
        

if __name__ == "__main__":
    user_input = sys.argv[1]
    format_file(user_input, True)

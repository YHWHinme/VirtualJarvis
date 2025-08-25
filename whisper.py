import whisper
import sys

def whisper_stt(input_file):
    model = whisper.load_model("turbo")
    result = model.transcribe(input_file)
    print(result["text"])
    return result["text"]

if __name__ == "__main__":
    user_text =  sys.argv[1]
    transcibe = whisper_stt(user_text)

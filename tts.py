from kokoro import KPipeline
import sys
from IPython.display import display, Audio
import os
import soundfile as sf
import random
import torch
pipeline = KPipeline(lang_code='a')


def speakText(input_text):
    # Defined variables
    random_number = random.randint(1, 10)  # Generate a random number between 1 and 10
    all_audio = []
    # Generating the audio
    generator = pipeline(input_text, voice='af_heart')
    for i, (gs, ps, audio) in enumerate(generator):
        # print(i, gs, ps)
        print(type(audio))
        if audio is not None and not isinstance(audio, str):
            all_audio.extend(list(audio))

    #Idk lol
    all_audio = torch.tensor(all_audio)
    display(Audio(data=all_audio, rate=24000, autoplay=True))

    # filename = "combined.wav"
    filename = f'combined_{random_number}.wav'
    sf.write(filename, all_audio, 24000)

    #simple system trial
    try:
        os.system(f"ffplay {filename} -autoexit -nodisp")
    except KeyboardInterrupt:
        print("Process interrupted")


    # Autoremove the file when it's over
    try:
        os.remove(filename)
        print("file removed")
    except OSError as e:
        print(f"Error deleting file: {e}")

def speakText_chunk(input_text):
    if not input_text.strip():
        return
    # Defined variables
    random_number = random.randint(1, 10)  # Generate a random number between 1 and 10
    all_audio = []
    # Generating the audio for the chunk
    generator = pipeline(input_text, voice='af_heart')
    for i, (gs, ps, audio) in enumerate(generator):
        if audio is not None and not isinstance(audio, str):
            all_audio.extend(list(audio))

    if not all_audio:
        return

    all_audio = torch.tensor(all_audio)
    display(Audio(data=all_audio, rate=24000, autoplay=True))

    filename = f'chunk_{random_number}.wav'
    sf.write(filename, all_audio, 24000)

    # Play the chunk
    try:
        os.system(f"ffplay {filename} -autoexit -nodisp")
    except KeyboardInterrupt:
        print("Process interrupted")

    # Remove the file
    try:
        os.remove(filename)
    except OSError as e:
        print(f"Error deleting file: {e}")


if __name__ == "__main__":
    custom_value = sys.argv[1]
    speakText(custom_value)

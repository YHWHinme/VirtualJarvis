import pyaudio
import numpy as np
import time
import threading
import queue
from gemini_model import gemini_chat_stream
from kokoro import KPipeline
import torch
import os  # For env checks if needed

# Initialize Kokoro pipeline
kokoro_pipeline = KPipeline(lang_code='a')

# Standalone TTS function
def generate_audio_from_text_standalone(text_chunk):
    all_audio = []
    generator = kokoro_pipeline(text_chunk, voice='af_heart')
    for _, _, audio in generator:
        if audio is not None and not isinstance(audio, str):
            all_audio.extend(list(audio))
    if all_audio:
        return torch.tensor(all_audio).numpy().astype(np.float32)
    return np.array([], dtype=np.float32)

def is_sentence_end(text):
    return text.strip() and text.strip()[-1] in '.!?'

# Jarvis class with streaming logic
class Jarvis:
    def __init__(self):
        self.stt_data = ""
        self.listening = False

    def think_stream(self):
        model_input = self.stt_data
        for chunk in gemini_chat_stream(model_input):
            yield chunk

    def modelAnswer_stream(self, chunk_generator):
        text_queue = queue.Queue()
        audio_queue = queue.Queue()

        # Producer: Feed AI chunks to text queue
        def ai_producer():
            buffer = ""
            for chunk in chunk_generator:
                buffer += chunk
                if is_sentence_end(buffer):
                    text_queue.put(buffer.strip())
                    buffer = ""
            if buffer:
                text_queue.put(buffer.strip())
            text_queue.put(None)

        # TTS Consumer
        def tts_consumer():
            while True:
                text_chunk = text_queue.get()
                if text_chunk is None:
                    audio_queue.put(None)
                    break
                audio_data = generate_audio_from_text_standalone(text_chunk)
                audio_queue.put(audio_data)

        # Playback Consumer
        def playback_consumer():
            py_audio = pyaudio.PyAudio()
            stream = py_audio.open(format=pyaudio.paFloat32, channels=1, rate=24000, output=True, frames_per_buffer=1024)
            while True:
                audio_data = audio_queue.get()
                if audio_data is None:
                    break
                for i in range(0, len(audio_data), 1024):
                    chunk = audio_data[i:i+1024]
                    stream.write(chunk.tobytes())
            stream.stop_stream()
            stream.close()
            py_audio.terminate()

        # Start threads (streaming enabled by default)
        producer_thread = threading.Thread(target=ai_producer)
        tts_thread = threading.Thread(target=tts_consumer)
        playback_thread = threading.Thread(target=playback_consumer)

        producer_thread.start()
        tts_thread.start()
        playback_thread.start()

        producer_thread.join()
        tts_thread.join()
        playback_thread.join()

    def Main(self):
        # Streaming mode enabled by default for concurrency
        # Benefits: Overlaps AI generation, TTS processing, audio playback using threads/queues
        streaming_mode = True  # Default true, no env var needed
        test_mode = True  # Use hardcoded input for testing

        if test_mode:
            self.stt_data = "Explain to me linear algebra"
            print(f"Test input: {self.stt_data}")
            if streaming_mode:
                chunk_gen = self.think_stream()
                self.modelAnswer_stream(chunk_gen)
            # Exit after test

# Main execution
if __name__ == "__main__":
    jarvis = Jarvis()
    jarvis.Main()
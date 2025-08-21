from faster_whisper import WhisperModel


# Model settings
model_size = "large-v3"
# Run on GPU with FP16
current_model = WhisperModel(model_size, device="cuda", compute_type="float16")

# or run on GPU with INT8
# model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
# or run on CPU with INT8
# model = WhisperModel(model_size, device="cpu", compute_type="int8")

def SpeechtoText(model=current_model):
    segments, info = model.transcribe("audio.mp3", beam_size=5)
    # print("Detected language '%s' with probability %f" % (info.language, info.language_probability))
    for segment in segments:
        # print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
        print(segment.text)

SpeechtoText()

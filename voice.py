import re
import sounddevice as sd
from faster_whisper import WhisperModel

SR = 16000

model = WhisperModel("small.en", device="cpu", compute_type="int8")

def _normalize(text):
  return re.sub(r"[^a-z0-9 ]", "", text.lower()).strip()

def listen(seconds=4):
  audio = sd.rec(int(seconds * SR), samplerate=SR, channels=1, dtype="float32")
  sd.wait()
  segments, _ = model.transcribe(
    audio.flatten(),
    language="en",
    beam_size=1,
    vad_filter=True,
    initial_prompt="Rei, Rei stop, Rei play, go sleep now, open terminal, workspace, volume up, volume down, quiet, louder",
  )
  text = "".join(s.text for s in segments)
  return _normalize(text)
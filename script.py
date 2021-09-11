from typing import Text
from gtts import gTTS
from playsound import playsound
import sys

print(sys.argv)
if len(sys.argv) > 1:
  text = sys.argv[1]
  speech = gTTS(text=text)
  speech.save("speech.mp3")
  playsound("speech.mp3")
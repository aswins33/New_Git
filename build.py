import os
from gtts import gTTS
a= "hello welcome to python programming "
speech=gTTS(text=a,lang='en')
speech.save("voice.mp3")
os.system("start voice.mp3")
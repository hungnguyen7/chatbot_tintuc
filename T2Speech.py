from gtts import gTTS
from playsound import playsound
import os

def text2speech(text):
    path = os.path.join(os.getcwd(),"audio" , r"voice.mp3")
    print(path)
    tex2voice = gTTS(text=text, lang='vi', slow=False)
    tex2voice.save(path)
    playsound(path)
    os.remove(path)

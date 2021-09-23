from gtts import gTTS
from playsound import playsound
import os
from pydub import AudioSegment
from pydub.playback import play
def text2speech(text, speed=1.0):
    path = os.path.join(os.getcwd(),"audio" , r"voice.mp3")
    print(path)
    tex2voice = gTTS(text=text, lang='vi', slow=False)
    tex2voice.save(path)

    # Play sound with playsound module
    # playsound(path)

    # Play sound with AudioSegment module
    sound = AudioSegment.from_file(path)
    audio_spd = speed_change(sound, speed)
    play(audio_spd)

    os.remove(path)

def speed_change(sound, speed=1.0):
    # Manually override the frame_rate. This tells the computer how many
    # samples to play per second
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
         "frame_rate": int(sound.frame_rate * speed)
      })
     # convert the sound with altered frame rate to a standard frame rate
     # so that regular playback programs will work right. They often only
     # know how to play audio at standard frame rate (like 44.1k)
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

# text2speech("Xin chào bạn tên gì, rất vui được biết bạn")
from playsound import playsound
def play_music(path):
    try:
        playsound(path)
    except: 
        print("An exception occurred") 
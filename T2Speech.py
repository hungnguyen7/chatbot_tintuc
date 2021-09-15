from playsound import playsound
def play_sound(path):
    try:
        playsound(path)
    except: 
        print("An exception occurred") 
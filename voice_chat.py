# Imports
#-----------
import requests
import json
import os

import speech_recognition as sr
from T2Speech import text2speech
bot_hearing = sr.Recognizer()


def run_dialogue():
    
    isContinue = True
    
    while isContinue:
        with sr.Microphone() as mic: 
            print("Bot: I'm hearing you...") 
            bot_hearing.adjust_for_ambient_noise(mic)
            # audio = bot_hearing.listen(mic) 
            audio = bot_hearing.record(mic, duration= 4)
            try:
                u_input = bot_hearing.recognize_google(audio, language="vi-VN")
            except:
                u_input = ""
        
               
        print("Customer: " + u_input)
        
        response = requests.post('http://localhost:5002/webhooks/rest/webhook', json={'message': u_input})
        bot_res=response.json()
        for i in bot_res:
            print("Bot response: \n" + i['text'])
            text2speech(i['text'])

run_dialogue()            
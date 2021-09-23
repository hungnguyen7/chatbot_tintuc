# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
# For custom action
import re
import requests
from bs4 import BeautifulSoup
import json
import list_event
from datetime import datetime

response = requests.get("https://tuoitre.vn/tin-moi-nhat.htm")
soup = BeautifulSoup(response.content, "html.parser")
# print(soup)
news_item = soup.findAll('li', class_='news-item')
# print(titles)
titles = [link.find('a').attrs["title"] for link in news_item]
titlesLinks = [link.find('a').attrs["href"] for link in news_item]
list_news = {}
list_titles = []
for x in range(0,10):
    list_news[str(x)] = 'https://tuoitre.vn' + titlesLinks[x]

file_name = ''
class action_get_newspaper(Action):
    def name(self) -> Text:
            return "action_get_newspaper"
    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            url = 'https://tuoitre.vn/tin-moi-nhat.htm'

            now = datetime.now()
            global file_name
            file_name = now.strftime("%d%m%Y%H%M%S")
            # print(file_name)
            with open('bot_calendar/{}.json'.format(file_name), 'w') as file:
                json.dump(list_news, file)

            for x in range(0, 10):
                res = str(x+1)+ "." + titles[x+1]
                # Text response
                dispatcher.utter_message(text=res)
                

            return []

class action_get_detail(Action):
    def name(self) -> Text:
            return "action_get_detail"
    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            # Tien hanh lay thong tin tu URL
            text = tracker.latest_message['text']
            arr_temp = text.split()
            url = ""
            # print(file_name)
            with open('bot_calendar/{}.json'.format(file_name), 'r') as file:
                    url_dict = json.load(file)
            for x in arr_temp:
                try:
                    if(int(x)):
                        url = url_dict[x]
                except:
                    continue
                        
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            htmlTags = soup.select_one('#main-detail-body')

            for filterOut in soup.find_all('div', { 'class': 'VCSortableInPreviewMode' }):
                filterOut.decompose()

            res = htmlTags.text
            # Text response
            dispatcher.utter_message(text=res)
            return []
        

class action_get_event_day(Action):
    def name(self) -> Text:
            return 'action_get_event_day'
    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        eventList = list_event.get_event_day()
        result = ""
        
        for item in eventList:      
            try:
                time = item.split("->")[0]
                event = item.split("->")[1]
                result += "Time: " + time  + "\nEvent: " + event + "\n"
            except:
                result = item
                break
        dispatcher.utter_message(text=result)
            
        return[]
    
class action_get_event_month(Action):
    def name(self) -> Text:
            return 'action_get_event_month'
    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
             
        eventList = list_event.get_event_month()
        result = ""
        
        for item in eventList:
            try:      
                time = item.split("->")[0]
                event = item.split("->")[1]
                result += "Time: " + time  + "\nEvent: " + event + "\n"
            except:
                result = item
                break
        dispatcher.utter_message(text=result)
        
            
        return[]
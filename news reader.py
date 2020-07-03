def speak(str):
   from win32com.client import Dispatch
   speak=Dispatch("SAPI.spVoice")
   speak.Speak(str)
if __name__ == "__main__":

   import requests
   import json,datetime
   print("News......")
   tt = datetime.datetime.now()
   rt = f"Date{tt.date()}, Time {tt.time()}, news"
   speak(rt)
   url = ('https://newsapi.org/v2/top-headlines?'
           'sources=bbc-sport&'
           'apiKey=49e391e7066c4158937096fb5e55fb5d')

   response = requests.get(url)
   text = response.text
   my_json = json.loads(text)
   for i in range(0, 101):
      speak(my_json['articles'][i]['title'])
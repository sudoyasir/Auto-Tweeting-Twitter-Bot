import json
import time
from requests.models import Response
import tweepy
import requests
import colored
from colored import stylize

auth = tweepy.OAuthHandler("consumer_key", "consumer_key_secret")
auth.set_access_token("bearer_token", "bearer_token_secret")

api = tweepy.API(auth)
try:
    api.verify_credentials()
    print("Authentication Successful!")
except:
    print("Error during Authentication!")

def scheduler():
    
    url = "https://api.quotable.io/random"
    response = requests.get(url)
    res = json.loads(response.text)
    print(res, colored.fg("blue"))
    api.update_status(res['content'])



  
# define the countdown func.
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer,colored.fg("green"), end="\r" )
        time.sleep(1)
        t -= 1
      
  
  
# input time in seconds
t = 1800
  
# function call

    
I = 0
while I<100:
    countdown(int(t))
    print("Tweet# ",I, colored.fg("red"))
    scheduler()
    print('     "TWEETED SUCCESFULLY!"', colored.fg("green"))
    I += 1
    

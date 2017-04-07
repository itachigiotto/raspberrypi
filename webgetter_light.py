#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import requests
from bs4 import BeautifulSoup
GPIO.setwarnings(False)
def get_html(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.text
    except:
        print("requests_wrong")
        return 0

def get_index(html,index):
    soup = BeautifulSoup(html,"html.parser")
    index[1] = (int(soup.find('span',attrs={"article-read"}).string))

def light():
    GPIO.output(26,1)
    time.sleep(0.5)
    GPIO.output(26,0)

index = [0,0]
GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT)
GPIO.output(26,0)
url = "http://www.zybuluo.com/itachigiotto/note/659241"
while True:
    html = get_html(url)
    get_index(html,index)
    if index[1]-index[0] > 1:
        print("got")
        light()
    else:
        print("waiting")
    index[0] = index[1]

import requests 
import os
import re
import time
import subprocess
from bs4 import BeautifulSoup
from asyncio import sleep
from random import choice
from telethon import events
from telethon.tl.types import Channel


#for getmusic
async def catmusic(cat , QUALITY):
  search = cat
  headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
  html = requests.get('https://www.youtube.com/results?search_query='+search, headers=headers).text
  soup = BeautifulSoup(html, 'html.parser')
  for link in soup.find_all('a'):
    if '/watch?v=' in link.get('href'):
        # May change when Youtube Website may get updated in the future.
        video_link = link.get('href') 
        break
  video_link =  'http://www.youtube.com/'+video_link
  if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
  command = ('youtube-dl -o "./temp/%(title)s.%(ext)s" --extract-audio --audio-format mp3 --audio-quality ' + QUALITY + ' ' + video_link)
  os.system(command)
  thumb = ('youtube-dl -o "./temp/%(title)s.%(ext)s" --write-thumbnail --skip-download ' + video_link)
  os .system(thumb)


async def catmusicvideo(cat):
    search = cat
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
    html = requests.get('https://www.youtube.com/results?search_query='+search, headers=headers).text
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a'):
        if '/watch?v=' in link.get('href'):
            # May change when Youtube Website may get updated in the future.
            video_link = link.get('href') 
            break    
    video_link =  'http://www.youtube.com/'+video_link
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    command = ('youtube-dl -o "./temp/%(title)s.%(ext)s" -f "[filesize<20M]" ' +video_link)  
    os.system(command)
    thumb = ('youtube-dl -o "./temp/%(title)s.%(ext)s" --write-thumbnail --skip-download ' + video_link)
    os .system(thumb)

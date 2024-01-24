from openai import OpenAI
import re 
import urllib.request
import requests
from openai import OpenAI
from dotenv import load_dotenv
import os
from pathlib import Path
from PIL import Image

def getLyrics(artist,song): 
    artist = artist.lower() 
    song = song.lower() 
    artist = re.sub('[^A-Za-z0-9]+', "", artist) 
    song = re.sub('[^A-Za-z0-9]+', "", song) 
    
    with urllib.request.urlopen("http://azlyrics.com/lyrics/"+str(artist)+"/"+str(song)+".html") as url:
        s = url.read()
        string = str(s)
        split = string.split('<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->') 
        split_html = split[1]
        split=split_html.split('</div>', 1)
        lyrics = split[0]
        lyrics = re.sub('(<.*?>)',"",lyrics) 
        filter_lyrics=lyrics.replace("\\n", " ")
        filter_lyrics=filter_lyrics.replace("\\'", "'")
        filter_lyrics=filter_lyrics.replace("\\r", "")
        return filter_lyrics


def generateImage(title, lyrics):
    load_dotenv()
    client = OpenAI()
    
    path_to_dir = os.path.dirname(os.path.abspath(__file__))
    path_to_assets=os.path.join(path_to_dir, "assets")
    if not os.path.exists(path_to_assets):
        os.makedirs(path_to_assets)
    
    response = client.images.generate(
        model="dall-e-3",
        prompt="create an album cover following these rules: Focus on specific, visually representable elements. Describe actions and scenarios rather than abstract concepts. Avoid ambiguous language that could be interpreted as including text. based on the following lyrics:" + lyrics,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url
    path_to_img = os.path.join(path_to_assets, title+'.jpg')

    img_data = requests.get(image_url).content
    with open(path_to_img, 'wb') as handler:
        handler.write(img_data)
    
    im = Image.open(path_to_img)
    im.show()

def imageFromSong(artist, title):
    song_lyrics=getLyrics(artist, title)
    generateImage(title, song_lyrics)



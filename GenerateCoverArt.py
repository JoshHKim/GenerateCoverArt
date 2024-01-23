from openai import OpenAI
import string 
import time 
import re 
import urllib.request
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def lyrics(artist,song): 
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



#artist = input("Enter an artist's name: ")
#title = input("Enter a song name: ")
song_lyrics=lyrics("coldplay", "vivalavida")

client = OpenAI()

response = client.images.generate(
    model="dall-e-3",
    prompt="create an album cover based on the following lyrics:" + song_lyrics,
    size="1024x1024",
    quality="standard",
    n=1,
)

image_url = response.data[0].url
print(image_url)

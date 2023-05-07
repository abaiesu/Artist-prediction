import time
from azapi import AZlyrics
from bs4 import BeautifulSoup
import requests


def get_lyrics(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        html_pointer = soup.find('div', attrs={'class': 'ringtone'})
        lyrics = html_pointer.find_next('div').text.strip()
        return lyrics
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Oops! Something went wrong:", err)


api = AZlyrics()
api.artist = "Lana Del Rey"
songs = api.getSongs()
lyrics_dict = {}

count =0

with open('Ultraviolence.txt', 'w') as f:
    for key, value in songs.items():
        if(count==68):
            break
        if 'url' in value:
            print(key)
            lyrics = get_lyrics(value['url'])
            if lyrics:
                count+=1
                lyrics_dict[key] = lyrics
                if(count>=52):
                    f.write(f"// {key} //\n\n{lyrics}\n\n")
            time.sleep(5)  # Add a 2-second delay between requests

print("Lyrics written to megadethsongs.txt")

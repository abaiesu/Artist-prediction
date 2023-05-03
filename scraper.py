from azapi import AZlyrics
from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_lyrics(url):
    html_page = urlopen(url)
    soup = BeautifulSoup(html_page, 'html.parser')
    html_pointer = soup.find('div', attrs={'class': 'ringtone'})
    lyrics = html_pointer.find_next('div').text.strip()
    print(lyrics)

api = AZlyrics()
api.artist = "megadeth"
songs = api.getSongs()
for key, value in songs.items():
    if 'url' in value:
        print(key)
        get_lyrics(value['url'])

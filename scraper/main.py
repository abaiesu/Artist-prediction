import os
import time
import re
import random
from azapi import AZlyrics
import requests
from bs4 import BeautifulSoup


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


def format_album_name(album_name):
    # Replace spaces with underscores and remove special characters from album names
    if not album_name:
        return "OtherSongs"
    album_name = re.sub(r'\W+', '', album_name)
    album_name = album_name.replace(' ', '_')
    return album_name


artists = ['Dead Can Dance', 'This Mortal Coil', 'Nick Drake', 'Bert Jansch', 'Fairport Convention',
           'John Martyn', 'Richard & Linda Thompson']


api = AZlyrics()

for artist in artists:
    count = 0  # reset the counter for each artist
    api.artist = ""  # reset the artist name before each iteration
    api.artist = artist.strip()
    songs = api.getSongs()
    if not isinstance(songs, dict):
        print(f"No songs found for {artist}")
        continue
    lyrics_dict = {}

    for key, value in songs.items():
        if count > 100:  # break the loop if we have scraped 150 songs
            break
        if 'url' in value:
            album = value['album']
            album_name = format_album_name(album)
            print(f"Scraping {key} from album {album}")
            lyrics = get_lyrics(value['url'])
            if lyrics:
                if album_name not in lyrics_dict:
                    lyrics_dict[album_name] = []
                lyrics_dict[album_name].append((key, lyrics))
                count += 1  # increment the counter
            time.sleep(random.randint(5, 15))  # Add a random delay between 5 and 15 seconds between requests

    if lyrics_dict:
        artist_dir = f"{api.artist}_lyrics"
        if not os.path.exists(artist_dir):  # check if the directory exists
            os.makedirs(artist_dir)

        for album, songs in lyrics_dict.items():
            with open(f"{artist_dir}/{album}.txt", "a+", encoding="utf-8-sig") as f:
                f.write(f"Album: {album}\n\n")
                for song in songs:
                    f.write(f"// {song[0]} //\n\n{song[1]}\n\n")

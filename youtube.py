import os

from pytube import YouTube as yt
from pytube import Search

# function to download an individual video as audio only

def Download(song_link, song_name, playlist_name):
    yt_obj = yt(song_link)
    yt_obj = yt_obj.streams.get_audio_only()
    try:
        yt_obj.download(output_path = './out/' + playlist_name, filename = song_name + '.mp3', skip_existing = True) # type: ignore
    except:
        print("An error has occurred")
    print("Download completed successfully")

# function to search for each song in the playlist and individually download it

def song_search(playlist, playlist_name):

    os.mkdir(path=f'./out/{playlist_name}')

    for song in playlist:
        search_query = song.title + ' - ' + song.artist 
        search = Search(search_query)
        link = 'http://youtube.com/watch?v=' + search.results[0].video_id # type: ignore
        Download(link, search_query, playlist_name)


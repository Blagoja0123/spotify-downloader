from spotify import set_song_list
from youtube import song_search

def main():
    link = input("Enter playlist URL: ")
    song_list, playlist_name = set_song_list(link)
    song_search(song_list, playlist_name)

if __name__ == '__main__':
    main()
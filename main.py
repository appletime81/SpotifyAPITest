import httpx
import base64
import configparser
from utils.get_token import get_spotify_token
from utils.get_playlist_songs import get_songs


def main():
    ini_file_path = "utils/settings.ini"
    token = get_spotify_token(ini_file_path)
    print(token)

    config = configparser.ConfigParser()
    config.read(ini_file_path)
    playlist_id = config.get("spotify", "playlist_id")
    get_songs(playlist_id, token)


main()

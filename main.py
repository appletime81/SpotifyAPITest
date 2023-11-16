import httpx
import base64
import configparser
from utils.get_token import get_spotify_token
from utils.get_playlist_songs import get_songs
from utils.stats import stats_songs_and_singers


def main():
    ini_file_path = "utils/settings.ini"
    token = get_spotify_token(ini_file_path)
    print(token)

    config = configparser.ConfigParser()
    config.read(ini_file_path)
    playlist_id = config.get("spotify", "playlist_id")
    ret = get_songs(playlist_id, token)
    stats_songs_and_singers(ret)


main()

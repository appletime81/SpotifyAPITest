import httpx
from pprint import pprint


def get_songs(playlist_id: str, token: str):
    ret = {
        "歌手": list(),
        "歌名": list(),
    }
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers = {"Authorization": f"Bearer {token}"}  # 請將這裡的令牌替換為你的實際令牌

    first_response = httpx.get(url, headers=headers)
    first_response_dict = first_response.json()
    total_numbers = first_response_dict.get("total")
    print(total_numbers)

    # limit is 100, need to correspond offset
    for i in range(0, total_numbers, 100):
        print(i)
        response = httpx.get(url + f"/?limit=100&offset={i}", headers=headers)
        temp_response_dict = response.json()
        items = temp_response_dict.get("items")

        for item in items:
            ret["歌名"].append(item.get("track").get("name"))
            ret["歌手"].append(
                item.get("track").get("album").get("artists")[0].get("name")
            )
    pprint(ret)
    print(len(ret.get("歌名")))
    print(len(ret.get("歌手")))

import httpx
import base64
import configparser


def get_spotify_token(ini_file: str):
    config = configparser.ConfigParser()
    config.read(ini_file)

    client_id = config.get("spotify", "client_id")  # 這裡填入你的 Spotify 客戶端 ID
    client_secret = config.get("spotify", "client_secret")  # 這裡填入你的 Spotify 客戶端密鑰

    # 將客戶端 ID 和密鑰進行 base64 編碼
    credentials = f"{client_id}:{client_secret}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()

    # 設置請求的頭部和資料體
    headers = {"Authorization": f"Basic {encoded_credentials}"}
    data = {"grant_type": "client_credentials"}

    # 發送 POST 請求
    response = httpx.post(
        "https://accounts.spotify.com/api/token", headers=headers, data=data
    )

    if response.is_success:
        body = response.json()
        token = body["access_token"]

        # save to ini file
        config.set("spotify", "token", token)

        # append to ini file
        with open("settings.ini", "w") as configfile:
            config.write(configfile)

        return token
    else:
        return False

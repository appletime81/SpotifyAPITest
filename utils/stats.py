import polars as pl


def stats_songs_and_singers(data):
    df = pl.DataFrame(data)

    # sort by `歌手` column
    df = df.sort("歌手")
    df = df.unique()

    # 統計`歌手`出現次數
    df_group_by_singer = df.group_by("歌手", maintain_order=True).agg(pl.count())

    # 存檔
    df.write_excel("songs.xlsx")
    df_group_by_singer.write_excel("歌手統計.xlsx")
    return "message: songs.xlsx is generated."

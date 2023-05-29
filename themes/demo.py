import requests
import json
# 获取歌曲信息
def get_song_info(song_id):
    url = 'http://music.163.com/api/song/detail/?id={}&ids=[{}]'.format(song_id, song_id)
    response = requests.get(url)
    song_info = json.loads(response.text)
    return song_
    # 获取歌曲评论
def get_song_comments(song_id):
    url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_{}'.format(song_id)
    response = requests.get(url)
    song_comments = json.loads(response.text)
    return song_comments
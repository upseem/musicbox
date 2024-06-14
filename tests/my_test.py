from NEMbox.api import NetEase
from NEMbox.api import Parse

import json
# 歌手 赵雷 6731

def test_api():
    api = NetEase()
    ids = [347230, 496619464, 405998841, 28012031]
    print(api.songs_url(ids))
    # print(api.songs_detail(ids))
    # print(Parse.song_url(api.songs_detail(ids)[0]))
    # user = api.login('example@163.com', md5(b'').hexdigest())
    # user_id = user['account']['id']
    # print(user)
    # api.logout()
    # print(api.user_playlist(3765346))
    # print(api.song_comments(347230))
    # print(api.search('海阔天空')['result']['songs'])
    # print(api.top_songlist()[0])
    # print(Parse.song_url(api.top_songlist()[0]))
    # print(api.djchannels())
    # print(api.search('测', 1000))
    # print(api.album(38721188))
    # print(api.djchannels()[:5])
    # print(api.channel_detail([348289113]))
    # print(api.djprograms(243, True, limit=5))
    # print(api.request('POST', '/weapi/djradio/hot/v1', params=dict(
    #     category='旅途|城市',
    #     limit=5,
    #     offset=0
    # )))
    # print(api.recommend_resource()[0])
    # print(api.songs_url([561307346]))
    print(api.playlist_songlist(96148442))
    
def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def my_api():
    api = NetEase()
    
    # 获取歌手所有歌
    # artist_id = 6731
    # artist_data = api.artists(artist_id)
    # print(json.dumps(artist_data, ensure_ascii=False, indent=4))
    # save_to_json(artist_data, 'artist_data.json')


    
    # 获取歌单详情
    playlist_id = 9961855233        #2312165875 民谣100首
    playlist_data = api.playlist_songlist(playlist_id)
    if playlist_data:
        print(json.dumps(playlist_data, ensure_ascii=False, indent=4))
        save_to_json(playlist_data, f'playlist_data_{playlist_id}.json')
    else:
        print(f"歌单{playlist_id}为空")   
        
    
    # 热门歌单
    # playlists_data = api.top_playlists()
    
    # if playlists_data:
    #     print(json.dumps(playlists_data, ensure_ascii=False, indent=4))
    #     save_to_json(playlists_data, f'playlists_data.json')
    # else:
    #     print(f"热门歌单为空")   
my_api()

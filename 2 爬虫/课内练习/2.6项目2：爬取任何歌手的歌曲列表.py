import requests

songer_name = input('请输入你想搜索的歌手名字：\n')

# 引用requests模块
#伪装请求头
header = {

    'origin': 'https://y.qq.com',
    'referer': 'https://y.qq.com/portal/search.html',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'

    }
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'

for x in range(1,4):

    param = {

        'ct': '24',

        'qqmusic_ver': '1298',

        'new_json': '1',

        'remoteplace': 'sizer.yqq.song_next',

        'searchid': '64405487069162918',

        't': '0',

        'aggr': '1',

        'cr': '1',

        'catZhida': '1',

        'lossless': '0',

        'flag_qc': '0',

        'p': x,

        'n': '10',

        'w': songer_name,

        'g_tk': '5381',

        'loginUin': '0',

        'hostUin': '0',

        'format': 'json',

        'inCharset': 'utf8',

        'outCharset': 'utf-8',

        'notice': '0',

        'platform': 'yqq.json',

        'needNewCode': '0'

    }

    res_songs= requests.get(url, params=param, headers=header)

    # 调用get方法，下载歌曲清单

    json_songs = res_songs.json()

    # 使用json()方法，将response对象，转为列表/字典

    # print(json_movie)

    list_songs = json_songs['data']['song']['list']

    for song in list_songs:


        url2 = 'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg'
        # 参数
        param2 = {

            'nobase64': '1',
            'musicid': song['id'],
            '-': 'jsonp1',
            'g_tk_new_20200303': '5381',
            'g_tk': '5381',
            'loginUin': '0',
            'hostUin': '0',
            'format': 'json',
            'inCharset': 'utf8',
            'outCharset': 'utf-8',
            'notice': '0',
            'platform': 'yqq.json',
            'needNewCode': '0'

        }
        # 伪装请求头
        header2 = {

            # 请求来源
            'origin': 'https://y.qq.com',
            # 请求来源
            'referer': 'https://y.qq.com/n/yqq/song/{}].html'.format(song['mid']),
            # 标记了请求从什么设备，什么浏览器上发出
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'

        }
        res2 = requests.get(url2, params=param2, headers=header2)
        json2 = res2.json()
        lyric = json2['lyric']
        # print(x, song['name'], song['id'])
        # # 输出的时候标记歌曲所在的页码和id
        # print(lyric)
        print('第{}页的歌曲《{}》,歌词是：{}\n'.format(x, song['name'], lyric))






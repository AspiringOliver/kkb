import requests
# print('第一页共有 {}个岗位\n'.format(len(list_post)))


url2 = 'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg'



#参数
param2 = {

    'nobase64': '1',
    'musicid': '447807',
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

#伪装请求头
header2 = {

    #请求来源
    'origin': 'https://y.qq.com',
    #请求来源
    'referer': 'https://y.qq.com/n/yqq/song/002M8hNI2QgtRY.html',
    # 标记了请求从什么设备，什么浏览器上发出
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'

    }

res = requests.get(url2, params=param2, headers= header2)
#print(res.text)
json_songs = res.json()
list_lyric = json_songs['lyric']
print(list_lyric)
#print(type(list_lyric))


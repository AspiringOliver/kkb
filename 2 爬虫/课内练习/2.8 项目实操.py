import requests, openpyxl
flag = 0
wb = openpyxl.Workbook()
sheet = wb.active
print('写下你喜欢的歌手和ta的杰作，获取歌迷们的热评吧！\n')
while 1:
    try:
        songer_name = input('请输入你想搜索的歌手名字：\n')
        song_name = input('请输入歌名：\n')
        sheet.title = song_name
        sheet['A1'] = '热门评论'
        list_name = ['ta的歌迷', '评论']
        sheet.append(list_name)

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
                #url2 = 'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg'
                url2 = 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg'
                # 参数
                param2 = {
                    'g_tk_new_20200303': '5381',
                    'g_tk': '5381',
                    'loginUin': '0',
                    'hostUin': '0',
                    'format': 'json',
                    'inCharset': 'utf8',
                    'outCharset': 'GB2312',
                    'notice': '0',
                    'platform': 'yqq.json',
                    'needNewCode': '0',
                    'cid': '205360772',
                    'reqtype': '2',
                    'biztype': '1',
                    'topid': song['id'], ##########
                    'cmd': '8',
                    'needmusiccrit': '0',
                    'pagenum': '0',
                    'pagesize': '25',
                    'lasthotcommentid':'',
                    'domain': 'qq.com',
                    'ct': '24',
                    'cv': '10101010'
                }
                '''param2 = {
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
                }'''
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
                #lyric = json2['lyric']
                hot_com = json2['hot_comment']['commentlist']
                if song['title_hilight'] == song_name:
                    flag = 1
                    for com in hot_com:
                        print('{} :\n  {}\n'.format(com['nick'], com['rootcommentcontent']))
                        list = [com['nick'], com['rootcommentcontent']]
                        sheet.append(list)
                        #print('第{}页的歌曲《{}》,歌词是：{}\n'.format(x, song['name'], lyric))
                    wb.save('热评——{}：{}.xlsx'.format(songer_name, song_name))
                    # 保存修改的Excel
                    wb.close()
        if flag == 0:
            print('\n%s没有唱过%s哟'%(songer_name, song_name))
        else:
            break
    except KeyError:
        print('不存在此歌手鸭？！')



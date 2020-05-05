#<RequestsCookieJar[<Cookie bid=xitC0b2dFVs for .douban.com/>]>
import requests


url = 'https://www.douban.com/'
# 创建session会话

session = requests.session()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'Cookie':  'bid=qgU0TgTGpyk; ll="118146"; __gads=ID=7f5899759b89940d:T=1587254240:S=ALNI_MZi1XRObCUyvbJF3ZSVbb6L2q7-1w; ct=y; __utmz=30149280.1587645684.4.4.utmcsr=xiaoke.kaikeba.com|utmccn=(referral)|utmcmd=referral|utmcct=/lesson/course/a43561de-a132-4603-8a63-8e7256294223/class/cf64c676-f937-41ff-8573-b21e0b9c5c0f; _vwo_uuid_v2=D0C81110E44218CB19F7951419389AFCE|c8b1d199ddfa2962995dd67b624c9948; _pk_ses.100001.8cb4=*; __utma=30149280.1752903154.1587254025.1587891126.1588417510.6; __utmc=30149280; ap_v=0,6.0; __yadk_uid=btx8nYmpI0P8sK48l1SSLEn4YsaaGq3u; push_noty_num=0; push_doumail_num=0; __utmv=30149280.21619; dbcl2="216195495:ZFV6eewa9/I"; ck=6n81; _pk_id.100001.8cb4=4db328ae6dcd5694.1588417507.1.1588420439.1588417507.; __utmb=30149280.47.10.1588417510'
}


comment_content = input('请输入发布内容')

data = {

    'ck': 'ALKz',

    'comment': comment_content,

    'privacy_and_reply_limit': 'P,'
}

res = session.post(url, data=data, headers=headers)
print(res)
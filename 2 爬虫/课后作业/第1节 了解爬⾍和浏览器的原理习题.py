import requests as re

res2 = re.get('https://www.baidu.com/img/bd_logo1.png')
photo = res2.content
with open('bd_logo1.png','ab') as b:
    b.write(photo)


#请求头Request Headers
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

#获取
res = re.get('https://baijiahao.baidu.com/s?id=1661382527708632196&wfr=spider&for=pc',headers=headers)
print(res.content.decode())
print('='*20)
print(type(res.content.decode()))#将二进制解码
print(type(res.content))
print(type(res.text))
with open('data.txt','ab') as v:
     v.write(res.content)


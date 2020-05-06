import requests
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}
url = 'https://movie.douban.com/chart'

res_movies = requests.get(url, headers=header)
print(res_movies)

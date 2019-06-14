import requests
from bs4 import BeautifulSoup

# 讀取網頁
request = requests.get('https://akacodedog.blogspot.com/')

# 解析 html 字串
html = BeautifulSoup(request.text, 'html.parser')

# 取得 blogger 的文章 title
post_title = html.select('.post-title a')

# 解析 html 的 a 結構
for i, t in enumerate(post_title):
    print((i + 1), '.', t.text, '(', t['href'], ')')
import re
import requests
import urllib.request
from selenium import webdriver

# pattern = re.compile(r'<a.*?href="(.*?)".*?title="(.*?)".*?>')
# resp = requests.get('https://www.douban.com')
# print(resp.status_code)
# if resp.status_code == 200:
#     all_matches = pattern.findall(resp.text)
#     print(all_matches)
#     for href, title in all_matches:
#         print(href)
#         print(title)

# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))

# r = requests.get('https://api.github.com/events')
# print(r.text)

# for page in range(1, 11):
#     resp = requests.get(
#         url=f'https://movie.douban.com/top250?start={(page-1)*25}',
#         headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}
#     )
#     # 我重点需要搞明白的就是requests.get到底返回了哪些内容
#     pattern1 = re.compile(r'<span class="title">([^&]*?)</span')
#     titles = pattern1.findall(resp.text)
#
#     pattern2 = re.compile(r'<span class="rating_num".*?>(.*?)</span>')
#     ranks = pattern2.findall(resp.text)
#
#     for title, rank in zip(titles, ranks):
#         print(title, rank)

browser = webdriver.Chrome()
browser.get('https://www.baidu.com/')
import requests
from lxml import etree

url = 'https://www.freesion.com/article/3879676853/'
heard = {
    'authority': 'www.freesion.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': '__51cke__=; JSESSIONID=75484564A42CDDC7ACC251CC7A45968E; __tins__20650105=%7B%22sid%22%3A%201685957374845%2C%20%22vd%22%3A%202%2C%20%22expires%22%3A%201685959370214%7D; __51laig__=3',
    'sec-ch-ua-platform': "Windows",

    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'

}
res = requests.get(url=url, headers=heard)
print(res.text)

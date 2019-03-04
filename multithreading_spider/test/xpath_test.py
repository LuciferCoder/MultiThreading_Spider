# coding=utf-8

import threading
import time
import requests
from lxml import etree
import json

url = 'http://www.fanjian.net/jiantu-5'
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/70.0.3538.67 Safari/537.36',
        }

items = []
r = requests.get(url=url, headers=headers)
content = r.text
tree = etree.HTML(content)
li_list = tree.xpath('//ul[@class="cont-list"]/li')
for i in li_list:
    title = i.xpath('./h2/a/text()')[0]
    img_url = i.xpath('./div/p/img/@data-src')
    item = {
        "title": title,
        "url": img_url
    }
    items.append(item)

print(items)

# for x in range(1, 5):
#     urls = url.format(x)
#     print(urls)
#     r = requests.get(url=urls, headers=headers)
#     content = r.text
#     tree = etree.HTML(content)
#     li_list = tree.xpath('//ul[@class="cont-list"]/li')
#     for i in li_list:
#         title = i.xpath('./h2/a/text()')[0]
#         img_url = i.xpath('./div/p/img/@data-src')
#         item = {
#             "title": title,
#             "url" : img_url
#         }
#         items.append(item)

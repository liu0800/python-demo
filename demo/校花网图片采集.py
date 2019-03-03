# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test
   Description :
   Author :       86138
   date：          2019/1/12
-------------------------------------------------
   Change Activity:
                   2019/1/12:
-------------------------------------------------
"""
import requests
from lxml import etree
import os
import random
import time

def get_html(url):

    time.sleep(random.randint(2,5))
    head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

    try:
        html = requests.get(url,headers = head)
        html.encoding = html.apparent_encoding
        if html.status_code == 200:
            print("成功获取源代码")

            return html.text
    except Exception as e:
        print("获取源代码失败")
        print(e)

def get_imgurl(html):

    html = etree.HTML(html)
    urls = html.xpath("//div[@class = 'img']//img[@width = '210']/@src")
    urllist = []
    Namelist = html.xpath("//div[@class = 'title']/span/a/text()")
    baseurl = 'http://www.xiaohuar.com'

    for url in urls:
        if baseurl not in url:
            url = baseurl + url
            urllist.append(url)
        else:
            urllist.append(url)

    return urllist,Namelist

def download_img(url,name,num):

    print("正在下载第%d张图片：%s"%(i + 1,url))

    head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

    html = requests.get(url, headers=head)
    html.encoding = html.apparent_encoding
    img = html.content
    suffix = url.split('.')[-1]

    with open(name + '.' + suffix,'wb')as f:
        f.write(img)


if __name__ == '__main__':

    if '校花图片' not in os.listdir():
        os.mkdir('校花图片')
    os.chdir('校花图片')

    url = 'http://www.xiaohuar.com/2014.html'
    html = get_html(url)
    urllist = get_imgurl(html)[0]
    Namelist = get_imgurl(html)[1]

    i = 0
    for url in urllist:
        download_img(url,Namelist[i],i)
        i += 1
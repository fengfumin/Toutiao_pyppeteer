# -*- coding: utf-8 -*-
# __author__="maple"
"""
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import csv
import time

from scrapy import Spider, Request
from bs4 import BeautifulSoup
from Toutiao_pyppeteer.cloud_word import *


class TaobaoSpider(Spider):
    name = 'toutiao'
    allowed_domains = ['www.toutiao.com']
    start_url = ['https://www.toutiao.com/','https://www.toutiao.com/search/?keyword={keyword}']

    tlist = ["https://www.toutiao.com/a6794863795366789636/",
             "https://www.toutiao.com/a6791790405059871236/",
             "https://www.toutiao.com/a6792756350095983104/",
             "https://www.toutiao.com/a6792852490845946376/",
             "https://www.toutiao.com/a6795883286729064964/",
             "https://www.toutiao.com/a6792888997241684492/",
             "https://www.toutiao.com/a6794685782792602124/",
             "https://www.toutiao.com/a6796583968398377485/",
             "https://www.toutiao.com/a6792897889786921485/",
             "https://www.toutiao.com/a6795916073163031043/",
             "https://www.toutiao.com/a6792805276564062728/",
             "https://www.toutiao.com/a6792805276564062728/",
             "https://www.toutiao.com/a6795916073163031043/",
             "https://www.toutiao.com/a6792897889786921485/",
             "https://www.toutiao.com/a6796583968398377485/",
             "https://www.toutiao.com/a6794685782792602124/",
             "https://www.toutiao.com/a6792888997241684492/",
             "https://www.toutiao.com/a6795883286729064964/",
             "https://www.toutiao.com/a6792852490845946376/",
             "https://www.toutiao.com/a6792756350095983104/",
             "https://www.toutiao.com/a6791790405059871236/",
             "https://www.toutiao.com/a6794863795366789636/",
             "https://www.toutiao.com/a6794863795366789636/",
             "https://www.toutiao.com/a6791790405059871236/",
             "https://www.toutiao.com/a6792756350095983104/",
             "https://www.toutiao.com/a6792852490845946376/",
             "https://www.toutiao.com/a6795883286729064964/",
             "https://www.toutiao.com/a6792888997241684492/",
             "https://www.toutiao.com/a6794685782792602124/",
             "https://www.toutiao.com/a6796583968398377485/",
             "https://www.toutiao.com/a6792897889786921485/",
             "https://www.toutiao.com/a6795916073163031043/",
             "https://www.toutiao.com/a6792805276564062728/"]

    def __init__(self, keyword, *args, **kwargs):
        super(TaobaoSpider, self).__init__(*args, **kwargs)
        self.keyword = keyword


    def open_csv(self):
        self.csvfile=open('train/data.csv', 'w', newline='', encoding='utf-8')
        fieldnames = ['title', 'comment']
        self.dict_writer = csv.DictWriter(self.csvfile, delimiter=',', fieldnames=fieldnames)
        self.dict_writer.writeheader()

    def close_csv(self):
        self.csvfile.close()

    def start_requests(self):
        for url in self.start_url:
            if 'search' in url:
                r_url = url.format(keyword=self.keyword)
            else:
                r_url=url
            yield Request(r_url, callback=self.parse_list)

    def parse_list(self, response):
        if "小米10" in response.text:
            soup = BeautifulSoup(response.text, 'lxml')  # 具有容错功能
            res = soup.prettify()  # 处理好缩进，结构化显示
            div_list=soup.find_all('div', class_='articleCard')
            # print(res)
            print(div_list)
            print(len(div_list))
            self.open_csv()
            for div in div_list:
                title=div.find('span',class_='J_title')
                self.dict_writer.writerow({"title":title.text})
                con=div.find('div',class_='y-left')
                self.dict_writer.writerow({"comment": con.text})

            print("关闭csv")
            self.close_csv()
            print("开始分词")
            text_segment()
            print("开始制图")
            chinese_jieba()




# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'

    # allowed_domains = ['python123.io']
    # start_urls = ['http://python123.io/ws/demo.html']

    def start_requests(self):
        urls = [
            'http://python123.io/ws/demo.html'
        ]

    # name = 'demo'  当前爬虫名字为demo
    # allowed_domains =  ```   爬取该网站域名以下的链接，该域名由cmd命令台输入
    # start_urls = [] 爬取的初始页面

    def parse(self, response):
        fname = response.url.split('/')[-1]
        with open(fname, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s.' % fname)

# scrapy crawl demo
# 报错
# pip3 install pypiwin32
#

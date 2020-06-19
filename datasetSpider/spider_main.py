#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 爬虫调度端

# URL管理器

# 添加新的URL到待爬取集合中
# 判断待添加URL是否在容器中
# 获取待爬取URL
# 判断是否还有待爬取URL
# 将URL从待爬取移动到已爬取

# 网页下载器
# urllib2
# requests

# 网页解析器

# 正则表达式
# html.parser
# BeautifulSoup
# lxml


# 分析目标
# URL格式
# 数据格式
# 网页编码
import sys
import os
import time
cur_path = os.path.abspath(os.path.dirname(__file__))
root_path = os.path.split(cur_path)[0]
sys.path.append(root_path)

from datasetSpider import url_manager, html_downloader, html_outputer, html_parser


class SpiderMain(object):

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        self.count_page_index = 0

    # 根据当前的链接爬取
    def craw(self):
        # 已完成的爬取数量
        page_index = -1
        page_count = 0
        # while self.urls.has_new_url():
        for _ in range(1):
            # time.sleep(1)
            # 设置进度条展示
            if page_index == -1:
                page_count = self.urls.get_new_length()
                page_index = 0
            new_url = self.urls.get_new_url()
            # 根据经历次数的不同增加超时时间判断
            overtime = self.urls.get_overtime()
            print ("start load")
            try:
                self.parser.parse_download(new_url)
                page_index = page_index + 1
                self.urls.set_overtime_empty()
                print ('finished %d / %d' % (page_index, page_count))

            except:
                # 存储没及时响应的url
                self.urls.add_bad_url(new_url)
                print ('%s craw download failed!' % (new_url))

        # self.outputer.output_html()

    def craw_url(self, root_url):
        page_index = 1
        host = 'sparse.tamu.edu'
        #考虑电脑内存，控制每次的最大页数
        while page_index < 2:
        # for page_index in range(1, 3):
            try:
                count = self.count_page_index * 20 + page_index
                url = root_url + '?page=' + str(count)
                print ('craw %d : %s ...' % (count, url))
                html_cont = self.downloader.download(url, host, 1)
                print ('post success!')
                urls = self.parser.parse_url(url, html_cont)
                print ('url success!')
                self.urls.add_new_urls(urls)
                page_index = page_index + 1
            except:
                print ('craw finally failed!')

        if self.urls.has_new_url():
            self.craw()


if __name__ == "__main__":
    root_url = "https://sparse.tamu.edu/"
    obj_spider = SpiderMain()
    obj_spider.craw_url(root_url)

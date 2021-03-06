#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import sys
import os
import time
cur_path = os.path.abspath(os.path.dirname(__file__))
root_path = os.path.split(cur_path)[0]
sys.path.append(root_path)

from newsSpider import url_manager, html_downloader, html_outputer, html_parser


class SpiderMain(object):

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        self.hundred_index = 0
    # 对已存在于数组中的url进行爬取
    def craw(self):
        # 已完成的爬取数量
        page_index = -1
        page_count = 0
        while self.urls.has_new_url():
        # for _ in range(5):
            time.sleep(2)
            # 设置进度条展示
            if page_index == -1:
                page_count = self.urls.get_new_length()
                page_index = 0
            new_url = self.urls.get_new_url()
            # 根据经历次数的不同增加超时时间判断
            overtime = self.urls.get_overtime()
            try:
                html_cont = self.downloader.download(
                    new_url, 'apnews.com',overtime)
                new_data = self.parser.parse(new_url, html_cont)
                self.outputer.output_word(new_data)
                # self.outputer.collect_data(new_data)
                page_index = page_index + 1
                self.urls.set_overtime_empty()
                print ('已完成 %d / %d' % (page_index, page_count))

            except Exception as err:
                # 回收没及时响应的url
                # self.urls.add_bad_url(new_url)
                print(err)
                print ('%s crawl failed' % (new_url))

        # self.outputer.output_html()
    # 从初始url中添加爬取的url，并调用爬取函数
    def craw_url(self, root_url):
        try:
            html_cont = self.downloader.download_url(root_url ,1)
            urls = self.parser.parse_url("https://apnews.com", html_cont)
            self.urls.add_new_urls(urls)
        except:
            print ('craw failed')
        # page_index = 1
        # 考虑电脑内存，控制每次的最大页数
        # while page_index < 5:
        # for page_index in range(1, 3):
        #     try:
        #         count = self.hundred_index * 100 + page_index
        #         url = root_url + str(count)
        #         print ('craw %d : %s' % (count, url))
        #         html_cont = self.downloader.download(url, 'www.qidian.com',1)
        #         print ('download success')
        #         urls = self.parser.parse_url(url, html_cont)
        #         self.urls.add_new_urls(urls)
        #         # page_index = page_index + 1
        #     except:
        #         print ('craw failed')

        if self.urls.has_new_url():
            self.craw()


if __name__ == "__main__":
    root_url = "https://apnews.com/apf-topnews"
    obj_spider = SpiderMain()
    obj_spider.craw_url(root_url)

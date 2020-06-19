#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import re
import urllib
from urllib.parse import urljoin
from bs4 import BeautifulSoup


class HtmlParser(object):

    # 直接下载数据
    def parse_download(self, page_url):
        print("page_url",page_url)
        f = urllib.urlopen(page_url)
        strlist = page_url.split('/')
        print("name",strlist[-1])
        with open(strlist[-1], "wb") as code:
            code.write(f.read())

    # 解析出数据的方法
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_data = self._get_new_data(page_url, soup)
        return new_data
    
    def _get_new_data(self, page_url, soup):

        f = urllib2.urlopen(page_url)
        strlist = page_url.split('/')
        with open(strlist[-1], "wb") as code:
            code.write(f.read())


    # 解析出url的方法
    def parse_url(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        return new_urls
    # 获取新的url
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find('table', class_='table table-sm table-striped').find_all('td', class_='column-download d-none d-lg-table-cell')
        # print(links)
        for link in links:
            new_url_list = link.find_all('a')
            new_url = new_url_list[-1]['href']
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls




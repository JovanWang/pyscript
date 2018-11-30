#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from newsSpider import html_downloader
import urllib.request as request
import time
from selenium import webdriver
import os


class HtmlParser(object):
    def __init__(self):
        self.downloader = html_downloader.HtmlDownloader()
        self.title_num = 0

    # 解析出数据的方法
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_data = self._get_new_data(page_url, soup)
        return new_data
    
    def _get_new_data(self, page_url, soup):
        res_data = {}
        res_data['title'] = ""
        res_data['text'] = []
        res_data['images_src'] = []
        self.title_num += 1
        res_data['title'] = str(self.title_num) + '-' + soup.find('div', class_='CardHeadline').find('h1').get_text()
        text_nodes = soup.find('div', class_='Article').findAll('p')
        for text_node in text_nodes:
            res_data['text'].append(text_node.get_text())
        if soup.find('div', class_='Content WireStory fluid-wrapper with-lead').find('a', class_='LeadFeature') != None:
            image_url = 'https://apnews.com' + soup.find('div', class_='Content WireStory fluid-wrapper with-lead').find('a', class_='LeadFeature')['href']
            #设置浏览器打开url
            browser = webdriver.Chrome()
            browser.get(image_url)
            image_html_cont =  browser.page_source
            browser.quit()
            # image_html_cont = self.downloader.download_image(image_url)
            image_html = BeautifulSoup(image_html_cont, 'html.parser')
            images = image_html.find('div', class_='ImageModal').find('div', class_='content').find('div', class_='image-slider').findAll('img')
            for image in images:
                image_src = image.get('src')
                if not os.path.exists("tempimage"):
                    os.makedirs("tempimage")
                if not os.path.exists("tempimage/" + res_data['title'][0:20]):
                    os.makedirs("tempimage/" + res_data['title'][0:20])
                image_path =  "tempimage/" + res_data['title'][0:20] + "/" + image_src.split("/")[-1]
                # print(image_path)
                request.urlretrieve(image_src, image_path)
                res_data['images_src'].append(image_path)
        
        return res_data
    # 解析出url的方法
    def parse_url(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        return new_urls

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find('article', class_='feed').find_all('div', class_='FeedCard WireStory with-image')

        for link in links:
            new_url = link.find('a', class_='headline')['href']
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls




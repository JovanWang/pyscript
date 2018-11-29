#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup


class HtmlParser(object):

    # 解析出数据的方法
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_data = self._get_new_data(page_url, soup)
        return new_data
    
    def _get_new_data(self, page_url, soup):
        res_data = {}
        res_data['name'] = ""
        res_data['text'] = []
        res_data['images'] = []
        res_data['name'] = soup.find('div', class_='search-input').find('input')["value"]
        print("当前内容:", res_data['name'])
        text_nodes = soup.find('div', id='pl_feedlist_index').findAll('div',class_="card-feed")
        for text_node in text_nodes:
            # tempCont = text_node.find('div', class_='content').find(attrs={'class':'txt','node-type':True})
            if text_node.find('div', class_='content').find(attrs={'node-type':'feed_list_content_full'}):
                res_data['text'].append(text_node.find('div', class_='content').find(attrs={'node-type':'feed_list_content_full'}).get_text())
            else:
                res_data['text'].append(text_node.find('div', class_='content').find(attrs={'node-type':'feed_list_content'}).get_text())
            # tempCont = text_node.find('div', class_='content').find(attrs={'class':'txt','node-type':True})
            imageList =  text_node.find('div', class_='content').find(attrs={'node-type':'feed_list_media_prev'}).findAll('img')
            for image in imageList:
                res_data['images'].append(image['src'])

        # name_node = soup.find('div', class_="book-info").find("em")
        # res_data['name'] = name_node.get_text()
        # intro_node = soup.find('div', class_="book-info").find("p", class_="intro")
        # res_data['intro'] = intro_node.get_text()
        # author_node = soup.find('div', class_="book-info").find('h1').find("a", class_="writer")
        # res_data['author'] = author_node.get_text()

        # res_data['type'] = ""
        # type_blue_nodes = soup.find('div', class_="book-info").find('p', class_="tag").find_all("span", class_="blue")
        # for type_blue_node in type_blue_nodes:
        #     res_data['type'] = res_data['type'] + type_blue_node.get_text() + ","
        # type_red_nodes= soup.find('div', class_="book-info").find('p', class_="tag").find_all("a", class_="red")
        # for type_red_node in type_red_nodes:
        #     res_data['type'] = res_data['type'] + type_red_node.get_text() + ","
        
        # res_data['tags'] = ""
        # tags_nodes = soup.find('div', class_="detail").find('p', class_="tag-wrap").find_all("a", class_="tags")
        # for tags_node in tags_nodes:
        #     res_data['tags'] = res_data['tags'] + tags_node.get_text() + ","

        # # 查找节点
        # count_node_em = soup.find('div', class_="book-info").find_all('p')[2].find_all('em')
        # count_node_cite = soup.find('div', class_="book-info").find_all('p')[2].find_all('cite')
        # word_count_text = count_node_em[0].get_text() + count_node_cite[0].get_text()
        # res_data['word_count'] = word_count_text
        # click_count_text = count_node_em[1].get_text() + count_node_cite[1].get_text()
        # res_data['click_count'] = click_count_text
        # groom_count_text = count_node_em[2].get_text() + count_node_cite[2].get_text()
        # res_data['groom_count'] = groom_count_text
        
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
        links = soup.find('div', class_='data').find_all('td', class_='td-02')

        for link in links:
            new_url = link.find('a')['href']
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls




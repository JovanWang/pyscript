#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import urllib
import urllib.request
from queue import Queue


class HtmlDownloader(object):
    
    def __init__(self):
        self.user_agent_que = Queue()
        self.user_agent_que.put('User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0')
        self.user_agent_que.put('User-Agent:Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50')
        self.user_agent_que.put('User-Agent:Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0')
        self.user_agent_que.put('User-Agent:Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)')
        self.user_agent_que.put('User-Agent:Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1')
        self.user_agent_que.put('User-Agent:Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1')
        self.user_agent_que.put('User-Agent:Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11')
        self.user_agent_que.put('User-Agent:Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11')
        self.user_agent_que.put('User-Agent:MQQBrowser/26Mozilla/5.0(Linux;U;Android2.3.7;zh-cn;MB200Build/GRJ22;CyanogenMod-7)AppleWebKit/533.1(KHTML,likeGecko)Version/4.0MobileSafari/533.1')
        self.user_agent_que.put('User-Agent:Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;AvantBrowser)')
    
    def download(self, url, host, overtime):
        if url is None:
            return None
        
        user_agent = self.user_agent_que.get()
        headers = {
            'Host': host,
            'User-Agent': user_agent
        }

        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req, timeout=5 + overtime*10)

        self.user_agent_que.put(user_agent)
        if response.getcode() != 200:
            return None

        return response.read()

    # 下载单个url
    def download_url(self, url, page_index):
        if url is None:
            return None

        headers = {
            'Host': 'sparse.tamu.edu',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
        }
        #参数
        values = {
            'cate':'realtimehot'
        }
        #进行参数封装
        data = urllib.parse.urlencode(values)
        url = url + '?' + data
        print ('craw %d : %s' % (page_index, url))
        response = urllib.request.urlopen(url, timeout=3)
        # print response.info()
        # response = urllib.request.urlopen(url, data=data, timeout=3)
        if response.getcode() != 200:
            return None

        return response.read()

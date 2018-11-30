#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import urllib
import urllib.request
from queue import Queue


class HtmlDownloader(object):
    
    def __init__(self):
        self.user_agent_que = Queue()
        self.user_agent_que.put('User-Agent:Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50')
        self.user_agent_que.put('User-Agent:Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50')
        self.user_agent_que.put('User-Agent:Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0')
        self.user_agent_que.put('User-Agent:Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)')
        self.user_agent_que.put('User-Agent:Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1')
        self.user_agent_que.put('User-Agent:Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1')
        self.user_agent_que.put('User-Agent:Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11')
        self.user_agent_que.put('User-Agent:Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11')
        self.user_agent_que.put('User-Agent:MQQBrowser/26Mozilla/5.0(Linux;U;Android2.3.7;zh-cn;MB200Build/GRJ22;CyanogenMod-7)AppleWebKit/533.1(KHTML,likeGecko)Version/4.0MobileSafari/533.1')
        self.user_agent_que.put('User-Agent:Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36')
    
    def download(self, url, host, overtime):
        if url is None:
            return None
        
        user_agent = self.user_agent_que.get()
        headers = {
            'Host': host,
            'User-Agent': user_agent
        }

        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req, timeout=10 + overtime*10)

        self.user_agent_que.put(user_agent)
        if response.getcode() != 200:
            return None
        return response.read()

    def baidu_transfer(self, param):
        url = "https://fanyi.baidu.com/basetrans"
        
        user_agent = self.user_agent_que.get()
        headers = {
            'Accept':'*/*',
            'Content-Type':'application/x-www-form-urlencoded',
            'Cookie':'BAIDUCUID=++; PSTM=1491655249; BIDUPSID=1ECA43D665529765134F5CCD000FB51A; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; hasSeenTips=1; BAIDUID=A57974B94365D8C0357D2613B4050312:FG=1; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; MCITY=-158%3A; BDUSS=kZLaWJsVDdCLVk4YklFR3ZJbGt-OFdrZXFLTGxBSkNZQXRzTGZTRFlsaThGaHBjQVFBQUFBJCQAAAAAAAAAAAEAAABQ6oU00NDV37OjyN0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALyJ8lu8ifJbW; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1422_21111_26350_27889_22074; BDSFRCVID=nbLOJeC626l72rQ7pkIIuFMPK2zRHN3TH6aoHPR1IWdIjKlHiLPxEG0PjU8g0Kubh02GogKKLmOTHpKF_2uxOjjg8UtVJeC6EG0P3J; H_BDCLCKID_SF=tJPHoDI-JKL3j5ruM-rV-JD0-fTBa4oXHD7yWCv8KqRcOR5Jj6K-h5bXKRLfbPnAW6Tl2xJcttcCOhuR3MA--t4n0bKDBlbbWCQiWpnVBUJWsq0x0-6le-bQypoaaT8H3KOMahv1al7xO-JoQlPK5JkgMx6MqpQJQeQ-5KQN3KJmhpFu-n5jHjj0Da_83H; delPer=0; PSINO=7; locale=zh; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1543476095; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1543476095; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1541765799,1543472813,1543476096; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1543476096',
            'Host':'fanyi.baidu.com',
            'User-Agent':user_agent
        }

        r = requests.post(url=url,data=param,headers=headers).json()
        if r == None:
            return None
        self.user_agent_que.put(user_agent)
        result = r['trans'][0]['dst']
        return result

    # 从启动网址中爬取url
    def download_url(self, url, page_index):
        if url is None:
            return None

        # headers = {
        #     'Host': 'apnews.com',
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
        # }
        #参数
        # values = {
        #     'cate':'realtimehot'
        # }
        #进行参数封装
        # data = urllib.parse.urlencode(values)
        # url = url + '?' + data
        print ('craw %d : %s' % (page_index, url))
        response = urllib.request.urlopen(url, timeout=10)
        # print response.info()
        # response = urllib.request.urlopen(url, data=data, timeout=3)
        if response.getcode() != 200:
            return None
        return response.read()

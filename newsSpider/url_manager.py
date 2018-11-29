#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
        self.bad_urls = set()
        self.overtime = 0

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        self.renovate_url()
        return len(self.new_urls) != 0


    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def add_bad_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.bad_urls:
            self.bad_urls.add(url)

    # 重新翻新
    def renovate_url(self):
        if len(self.new_urls) == 0 and len(self.bad_urls) != 0 and self.overtime < 5:
            if len(self.bad_urls) == len(self.old_urls):
                self.overtime += 1
            self.old_urls.clear()
            self.new_urls = self.new_urls | self.bad_urls
            self.bad_urls.clear()

    
    def get_new_length(self):
        return len(self.new_urls)

    def get_overtime(self):
        return self.overtime
    def set_overtime_empty(self):
        self.overtime = 0




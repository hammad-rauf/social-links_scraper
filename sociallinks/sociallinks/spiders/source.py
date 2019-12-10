from scrapy import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

import xlrd

import pandas as pd

from datetime import date

from ..items import SociallinksItem

class SocialLinkSpider(CrawlSpider):

    name = "sociallinks"

    socials = ["facebook","whatsapp","linkedin","instagram","twitter","skype","pinterest","telegram","wechat","qq","tumblr","reddit","xing","flickr","youtube"]

    rows = 0

    ignore = []

    def __init__(self, config_file = None, *args, **kwargs):                    
        super(SocialLinkSpider, self).__init__(*args, **kwargs)   

        loc = (config_file) 

        self.df = pd.read_excel(loc)

        self.n = len(self.df)          

        self._config = []

        for a in range(self.n):
            link = self.df.iloc[a]["Website"]

            if str(link) != "nan":
                self._config.append(link) 

            self._url_list = self._config                                                               

    def start_requests(self):    

        for url in self._url_list:                                              
            yield Request(url = url, callback = self.parse)
   
    def parse(self, response):

        links = SociallinksItem()

        for a in range(self.n):

            if self.df.iloc[a]["Website"] == response.url:        

                links["Adresse"] = self.df.iloc[a]["Adresse"]
                links["Email"] = self.df.iloc[a]["Email"]
                links["Telefon"] =  self.df.iloc[a]["Telefon"]
                links["Website"] = self.df.iloc[a]["Website"]

                break
             
        for social in self.socials:
            links[social] = response.css(f"a[href*='{social}']::attr(href)").extract_first()


        yield links

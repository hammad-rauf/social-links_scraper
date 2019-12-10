# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SociallinksItem(scrapy.Item):

    Adresse = scrapy.Field()
    Email = scrapy.Field()
    Telefon =  scrapy.Field()
    Website = scrapy.Field()
    
    facebook = scrapy.Field()
    whatsapp = scrapy.Field()
    linkedin = scrapy.Field()
    instagram = scrapy.Field()
    twitter = scrapy.Field()
    skype = scrapy.Field()
    pinterest = scrapy.Field()
    telegram = scrapy.Field()
    wechat = scrapy.Field()
    qq = scrapy.Field()
    tumblr = scrapy.Field()
    reddit = scrapy.Field()
    xing = scrapy.Field()
    flickr = scrapy.Field()
    youtube = scrapy.Field()
    pass

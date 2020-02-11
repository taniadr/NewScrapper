#!/usr/bin/python
# -*- encoding:utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from CheckProducts.items import NewsItem

class CheckProductsSpider(scrapy.Spider):
	name = 'g1'
	start_urls = ['https://g1.globo.com']

	

	def parse(self, response):
		print 'ACESSANDO URL: %s' % response.url
		#Titulo da Noticia:
		response.xpath('normalize-space(//div[contains(@class,"feed-post-body-title")]/div/div/a/text())').extract()
		#Body da Noticia:
		response.xpath('normalize-space(//div[@class="feed-post-body-resumo"]/div)').extract()
		#Link da Noticia:
		response.xpath('normalize-space(//div[contains(@class,"feed-post-body-title")]/div/div/a/@href)').extract()
		#Link da Imagem (arrumar com bs4)
		image = response.xpath('//picture[@class="bstn-fd-cover-picture"]/img').extract_first()



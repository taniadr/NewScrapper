#!/usr/bin/python
# -*- encoding:utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from CheckProducts.items import NewsItem
from scrapy.exceptions import CloseSpider

class Printer():
    """Print things to stdout on one line dynamically"""
    def __init__(self,data):
        sys.stdout.write("\r"+data.__str__())
        sys.stdout.flush()

class CheckProductsSpider(scrapy.Spider):
	name = 'spider'
	start_urls = ['https://g1.globo.com']
	item_count = 0


	def start_request(self):
		return scrapy.Request(start_url, callback=self.parse)


	def parse(self, response):
		print 'ACESSANDO URL: %s' % response.url
		NewNode = NewsItem()
		#Titulo da Noticia:
		NewNode['title'] = response.xpath('normalize-space(//div[contains(@class,"feed-post-body-title")]/div/div/a/text())').extract() 
		#Body da Noticia:
		NewNode['body'] = response.xpath('normalize-space(//div[@class="feed-post-body-resumo"]/div)').extract()
		#Link da Noticia:
		NewNode['link'] = response.xpath('normalize-space(//div[contains(@class,"feed-post-body-title")]/div/div/a/@href)').extract()
		#Link da Imagem (arrumar com bs4)
		NewNode['image'] = response.xpath('//picture[@class="bstn-fd-cover-picture"]/img').extract_first()

		self.item_count += 1

		if self.item_count > 3:
			raise CloseSpider('Concluido')

		yield NewNode

	def exportJSON():
		f_json = open("itens.json",'w')
		with open("itens.json", "w") as myfile:
			myfile.write(json.dumps(grab(),sort_keys=False))
		myfile.close()
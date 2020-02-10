#!/usr/bin/python
# -*- encoding:utf-8 -*-
import scrapy
from CheckProducts.items import CheckproductsItem

class CheckProductsSpider(scrapy.Spider):
	name = 'checkproducts'
	product = 'mala'
	start_urls = ['https://lista.mercadolivre.com.br/']

	if product:
		start_urls = ['%s/%s#D[A:%s]' % (start_urls, product, product)]


	def parse(self, response):
		ml_anuncio = CheckproductsItem()
        ml_anuncio['name'] = response.xpath('normalize-space(//h1[@class="item-title__primary "]/text())').extract_first()
        ml_anuncio['link'] = response.url
        ml_anuncio['price'] = response.xpath('normalize-space(//span[@class="price-tag-fraction"]/text())').extract()
        #ml_anuncio['price_d'] = response.xpath('normalize-space(//span[@class="price-tag-fraction"]/text())').extract()
        ml_anuncio['store'] = response.xpath('//*[contains(@class, "reputation-view-more")]/@href').extract()
        ml_anuncio['state'] = response.xpath('normalize-space(//div[@class="item-conditions"]/text())').extract()


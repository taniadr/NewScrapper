#!/usr/bin/python
# -*- encoding:utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from CheckProducts.items import NewsItem

class Printer():
    """Print things to stdout on one line dynamically"""
    def __init__(self,data):
        sys.stdout.write("\r"+data.__str__())
        sys.stdout.flush()

class CheckProductsSpider(scrapy.Spider):
	name = 'g1'
	start_urls = ['https://g1.globo.com']

	def

	def parse(self, response):

		#condicao para loop


		print 'ACESSANDO URL: %s' % response.url
		#Titulo da Noticia:
		response.xpath('normalize-space(//div[contains(@class,"feed-post-body-title")]/div/div/a/text())').extract()
		#Body da Noticia:
		response.xpath('normalize-space(//div[@class="feed-post-body-resumo"]/div)').extract()
		#Link da Noticia:
		response.xpath('normalize-space(//div[contains(@class,"feed-post-body-title")]/div/div/a/@href)').extract()
		#Link da Imagem (arrumar com bs4)
		image = response.xpath('//picture[@class="bstn-fd-cover-picture"]/img').extract_first()

		#condição de parada
		#yield
		#export
	

	def saveImage(path):
		directory = directory = os.path.dirname(os.path.realpath(__file__)) + '\images_ml'

		if not os.path.exists(directory):
			os.makedirs(directory)
		
		image_file = str(uuid.uuid1()) +'.jpg'
		f = open( directory + '\\' + image_file,'wb')
		content = requests.get(path).content
		
		f.write(content)
		f.close()
		
		return image_file

	def exportJSON():
		f_json = open("itens.json",'w')
		with open("itens.json", "w") as myfile:
			myfile.write(json.dumps(grab(),sort_keys=False))
		myfile.close()


>>> for titulos in response.xpath('//span[@class="main-title"]/text()'):
...     text_title =titulos.get()
...     price = 1
...     link = response.url
...     print(dict(text_title=text_title, price=price, link=link))


====

for titulos in response.xpath('//span[@class="main-title"]/text()'):
	title = titulos.get()
	price = titulos.xpath('//span[@class="item__brand-title-tos"]/span/text()').get()
	store = titulos.xpath('//span[@class="item__brand-title-tos"]/span/text()').get()		
	print(dict(title=title, price=price))




=== working on this now 
for membro in response.css('li.results-item'):
	titulo = membro.xpath('//span[@class="main-title"]/text()').get()
	price = membro.xpath('//span[@class="price__fraction"]/text()').get()
	store = membro.xpath('//span[@class="item__brand-title-tos"]/span/text()').get()
	print(dict(titulo=titulo, price=price, store=store))

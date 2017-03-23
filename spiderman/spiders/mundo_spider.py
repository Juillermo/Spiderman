import scrapy
from scrapy.loader import ItemLoader
from spiderman.items import MundoItem

class MundoSpider(scrapy.Spider):
    name = "mundo"

    def start_requests(self):
        url = 'http://www.elmundo.es/' # starts at main page
	yield scrapy.Request(url, self.ini_parse)

    def ini_parse(self, response):
	# enter each section
	for href in response.xpath('//*[@data-section]/a/@href').extract():
            yield scrapy.Request(response.urljoin(href), callback=self.cont_parse)

    def cont_parse(self, response):
	# enter the articles of the section
	#head = response.xpath('//*[@itemprop="headline"]/a/@href').extract()
	#yield scrapy.Request(response.urljoin(head[0]), callback=self.parse)
        for headline in response.xpath('//*[@itemprop="headline"]/a/@href').extract():
            yield scrapy.Request(response.urljoin(headline), callback=self.parse)

    def parse(self, response):
	# get title and body of the article
	l = ItemLoader(item=MundoItem(), response=response)
	l.add_xpath('Title', '//*[@itemprop="headline"]/text()')
	l.add_xpath('Body', '//div[@itemprop="articleBody"]/p[not(@*)]/descendant-or-self::*/text()')
	return l.load_item()



#   ---------
#   Garbage
#   ---------

# #For parsing only the first article of each section-------------
#
#   def cont_parse(self, response):
#	head = response.xpath('//*[@itemprop="headline"]/a/@href').extract()
#	yield scrapy.Request(response.urljoin(head[0]), callback=self.parse)

# #Exporting the parse elements in a json------------
#
#	yield {
#		'Title': response.xpath('//*[@itemprop="headline"]/text()').extract_first(),
#               'Body': response.xpath('//div[@itemprop="articleBody"]/p[not(@*)]/descendant-or-self::*/text()').extract(),
#            }


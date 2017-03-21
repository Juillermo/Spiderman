import scrapy

class QuotesSpider(scrapy.Spider):
    name = "mundo"

    def start_requests(self):
        url = 'http://www.elmundo.es/'
	yield scrapy.Request(url, self.ini_parse)

    def ini_parse(self, response):
	for href in response.xpath('//*[@data-section]/a/@href').extract():
            yield scrapy.Request(response.urljoin(href), callback=self.parse)

    def parse(self, response):
        for headline in response.xpath('//*[@itemprop="headline"]/a'):
            yield {
		'section': response.xpath('//title/text()').extract_first(),
                'text': headline.xpath('./text()').extract_first(),
		'link': headline.xpath('./@href').extract_first(),
            }

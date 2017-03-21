import scrapy

class QuotesSpider(scrapy.Spider):
    name = "mundo"

    def start_requests(self):
        url = 'http://www.elmundo.es/'
	yield scrapy.Request(url, self.ini_parse)

    def ini_parse(self, response):
	for href in response.css('li.tab a::attr(href)').extract():
            yield scrapy.Request(response.urljoin(href), callback=self.parse)

    def parse(self, response):
        for normal in response.css('h3.mod-title.normal'):
            yield {
		'section': response.css('title::text').extract_first(),
                'text': normal.css('a::text').extract_first(),
		'link': normal.css('a::attr("href")').extract_first(),
            }

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from elasticsearch import Elasticsearch # For sending articles to ElasticSearch database

class MundoPipeline(object):
	
    def __init__(self):

	self.es = Elasticsearch(['http://ec2-52-202-185-94.compute-1.amazonaws.com:9200/',]) # host of database


    def process_item(self, item, spider):
	
	# collapse body

	body = ''
	for el in item['Body']:
		body = body + el

	doc = { 'Title': item['Title'][0], 'Body': body }
	

	# check whether doesn't exist article with same title and send it

	query = {
		"query":{"match_phrase":{"Title":doc['Title']}},
		"_source":"Title",
		"size":1
	}

	res = self.es.search(index="el-mundo", body=query)

	if not res['hits']['total']:
		res = self.es.index(index="el-mundo", doc_type='Article', body=doc) # send to database
        return item

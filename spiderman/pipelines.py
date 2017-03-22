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

	doc = {
	    'Title': item['Title'],
    	    'Body': item['Body'],
	}

	res = self.es.index(index="el-mundo", doc_type='Article', body=doc) # send to database
        return item

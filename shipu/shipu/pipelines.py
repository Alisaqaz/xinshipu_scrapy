# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ShipuPipeline(object):
    def process_item(self, item, spider):
    	with open('shipu_list.txt','a') as file:
    		line=u"{0}: \nname:{1}\n step:{2}\n\n\n".format(item['id'],item['name'],item['step'])
    		file.write(line)
    	return item

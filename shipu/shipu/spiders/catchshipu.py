import scrapy
from shipu.items import ShipuItem
from scrapy.selector import Selector
from scrapy.http import Request

class ShipuSpider(scrapy.Spider):
	name="catchshipu"
	allowed_domains=["xinshipu.com"]
	start_urls=['https://www.xinshipu.com/zuofa/1111']
	def parse(self,response):
		#filename="info.html"
		#open(filename,'wb+').write(response.body)
		hxs=Selector(response)
		item=ShipuItem()
		r=hxs.xpath('//h1[@class="font16 h47 tc cg1"]/text()\n').extract()
		item['name']=r[0] if r else None
		Steps=hxs.xpath('//div[@class="swipeboxEx mlr1 bbm"]')
		id=hxs.xpath('//*[@id="shipuid"]/@value').extract()
		item['id']=id[0] if id else None
		step=''
		for v in Steps.xpath('.//p/text()\n'):
			step=step+v.extract().strip()
		item['step']=step
		yield item
		num=1111
		while (num<88888):
			num=num+1
			str_num=str(num)
			url="https://www.xinshipu.com/zuofa/"+str_num
			yield Request(url,callback=self.parse,dont_filter=True)
		
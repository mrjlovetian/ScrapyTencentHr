# -*- coding: utf-8 -*-
import scrapy

from tencent.items import TencentItem


class TenxunSpider(scrapy.Spider):
    name = 'tenxun'
    allowed_domains = ['hr.tencent.com']
    url = "https://hr.tencent.com/position.php?&start="
    offset = 0
    start_urls = [url+str(offset)]

    def parse(self, response):

        position_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        if len(position_list) != 0:
            for position in position_list:
                item = TencentItem()

                item['positionName'] = position.xpath("./td[1]/a/text()")[0].extract()

                if len(position.xpath("./td[2]/text()")) != 0:
                    item['positionType'] = position.xpath("./td[2]/text()")[0].extract()
                else:
                    item['positionType'] = ""
                item['peropleNumber'] = position.xpath("./td[3]/text()")[0].extract()
                item['positionLocation'] = position.xpath("./td[4]/text()")[0].extract()
                item['publishTime'] = position.xpath("./td[5]/text()")[0].extract()

                yield item
                print('positionNmae', item['positionName'], item['positionType'], item['peropleNumber'],
                      item['positionLocation'], item['publishTime'])

            self.offset += 20
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)


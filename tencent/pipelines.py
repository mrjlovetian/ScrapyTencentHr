# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class TencentPipeline(object):

    def __init__(self):
        self.f = open("tencent.json", "w")

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii = False) + ",\n"
        self.f.write(content)
        print("这里是不是都没有进来啊");
        return item

    def close_spider(self, spider):
        print("lai l meiyou a")
        self.f.close()

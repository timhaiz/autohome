# -*- coding: utf-8 -*-
import json, codecs
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class TutorialPipeline(object):
    def __init__(self):  # 添加一下初始化方法
        self.file = codecs.open('item.json', 'wb', encoding='utf-8')
        # item.json指的是你要保存的json格式文件的名称，编码格式一般都是'utf-8'

    def process_item(self, item, spider):
        line = json.dumps(dict(item),
                          ensure_ascii=False) + '\n'
        # 这一句会将你每次返回的字典抓取出来
        # “ensure_ascii=False”这一句话很重要，如果是True的话就是我们保存的\u4e2d\u56fd这种格式了
        self.file.write(line)  # 写入到文件中
        return item
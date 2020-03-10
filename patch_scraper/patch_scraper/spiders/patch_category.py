# -*- coding: utf-8 -*-
import scrapy


class PatchCategorySpider(scrapy.Spider):
    name = "patch_category"
    start_urls = [
        "https://www.pathofexile.com/forum/view-thread/2753887"
    ]

    def parse(self, response):
        #last 3 are report/additional info so we exclude

        content = response.css("div.content")[0]
        out = {}
        out['changes'] = []
        out['headings'] = []

        for category in content.css("strong::text")[:-3]:
            out['headings'].append(category.get())

        for change in content.css('li::text'):
            out['changes'].append(change.get())
        yield out 

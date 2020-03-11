# -*- coding: utf-8 -*-
import scrapy


class PatchCategorySpider(scrapy.Spider):
    name = "patch_category"
    start_urls = [
        "https://www.pathofexile.com/search/results/Content+Update/search-within/threads/forums/366/page/1"
    ]

    def parse(self, response):
        author_page_links = response.css('td.content div.content a')
        yield from response.follow_all(author_page_links, self.parse_patch_notes)

        pagination_links = response.css('div.pagination a')
        yield from response.follow_all(pagination_links, self.parse)


    def parse_patch_notes(self, response):
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


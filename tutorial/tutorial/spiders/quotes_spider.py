# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    cnt = 0
    def start_requests(self):
        urls = [
            'https://jstris.jezevec10.com/'
        ]
        for url in urls:
            print(url)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        # print(QuotesSpider.cnt)
        # QuotesSpider.cnt += 1
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
# class ExampleSpider(scrapy.Spider):
#     name = "quotes"
#     cnt = 0
#     def start_requests(self):
#         urls = [
#             'https://vi.jstris.jezevec10.com/'
#         ] * 2
#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)

#     def parse(self, response):
#         # print(QuotesSpider.cnt)
#         # QuotesSpider.cnt += 1
#         print(response.body)
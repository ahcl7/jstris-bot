import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    cnt = 0
    def start_requests(self):
        urls = [
            'https://vi.jstris.jezevec10.com/'
        ] * 2
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(QuotesSpider.cnt)
        QuotesSpider.cnt += 1
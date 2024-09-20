import scrapy


class AllquotesSpider(scrapy.Spider):
    name = "allquotes"
    allowed_domains = ["quotes.org"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        smalltag = response.css('small ::text').getall()
        print()
        print()
        print()
        print('smalltag',smalltag)
        print()
        print()


        pass

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

        for author in smalltag:
            print()
            print('author', author)
            print()
        print()
        print()


        pass

import scrapy
import json


class AuthorsSpider(scrapy.Spider):
    name = "authors_spider"
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        author_urls = response.css('.author + a::attr(href)').getall()
        for url in author_urls:
            yield response.follow(url, self.parse_author)

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_author(self, response):
        yield {
            'name': response.css('h3.author-title::text').get().strip(),
            'birthdate': response.css('.author-born-date::text').get(),
            'bio': response.css('.author-description::text').get().strip()
        }

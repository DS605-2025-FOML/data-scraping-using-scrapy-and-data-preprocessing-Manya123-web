# scraper_demo/spiders/scraper_demo.py
import scrapy
from ..items import ScraperDemoItem

class QuotesSpider(scrapy.Spider):
    name="quotes"
    start_urls=['https://quotes.toscrape.com']
    
    
    def parse(self,response):
        # This method is used to handle responses downloaded 
        all_div_quotes=response.css('div.quote')
        # creates an instance
        for quote_info in all_div_quotes:
            items=ScraperDemoItem()
            text=quote_info.css('span.text::text').extract_first()
            author=quote_info.css('.author::text').extract_first()
            tags=quote_info.css('.tag::text').extract()     
            items['text']=text
            items['author']=author
            items['tags']=tags
            yield items
        next_page=response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)
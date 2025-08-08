import scrapy
from ..items import Books

class Books_Details(scrapy.Spider):
    name="books"
    start_urls=['https://books.toscrape.com/catalogue/category/books_1/index.html']
    
    def parse(self,response):
        all_books_info=response.css('article.product_pod')
        for books_det in all_books_info:
            items=Books()
            book_cover=books_det.css('img::attr(src)').extract()
            book_cover[0]=book_cover[0].replace("../../../","https://books.toscrape.com/")
            ratings=books_det.css('p.star-rating::attr(class)').get()
            ratings=ratings.split()[-1]
            book_name=books_det.css('h3 a::attr(title)').extract()
            price=books_det.css('.price_color::text').extract()
            stock_availability=books_det.css('.availability::text').extract()
            stock_availability=[text.strip() for text in stock_availability if text.strip()]
            items['book_cover']=book_cover
            items['ratings']=ratings
            items['book_name']=book_name
            items['price']=price
            items['stock_availability']=stock_availability
            yield items
        
        next_page=response.css('li.next a::attr(href)').get()
        
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)

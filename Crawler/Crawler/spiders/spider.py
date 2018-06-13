import scrapy

class RarbgSpider(scrapy.Spider):
    name = "rarbg"

    def start_requests(self):
        urls = ['https://rarbg.is/torrents.php']
        for url in urls:
            yield scrapy.Request(url=url, callable=self.parse)
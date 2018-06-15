import scrapy
import os
import os.path as path

class RarbgSpider(scrapy.Spider):
    name = "rarbg"
    # start_urls = ['http://www.hfnu.edu.cn/']
    start_urls = ['https://rarbg.is/torrents.php']

    def parse(self, response):
        url = response.url;
        body = response.body;
        try:
            f = open(path.join(os.getcwd(), self.name + '.html'), 'wb');
            f.write(body)
            f.close()
        except Exception as e:
            print e
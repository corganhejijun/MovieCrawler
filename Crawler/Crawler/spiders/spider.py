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
            headList = response.xpath('/html/body/table[3]/tbody/tr/td[2]/div/table/tbody/tr[2]/td/div[1]/table/tbody/tr/td/a/@href').extract()
            for subUrl in headList:
                next_page = response.urljoin(subUrl)
                yield scrapy.Request(next_page, callback=self.parseMovie)
        except Exception as e:
            print e

    def parseMovie(self, response):
        url = response.url;
        body = response.body;
        try:
            title = response.css("h1.black::text").extract_first()
            print "############# title is: {}".format(title)
            tableList = response.css("div.content-rouned table.lista-rounded table.lista tbody tr").extract()
            for tr in tableList:
                if tr.find('IMDB Rating') > 0:
                    print "############ imdb rating is: ".format(tr)
        except Exception as e:
            print e
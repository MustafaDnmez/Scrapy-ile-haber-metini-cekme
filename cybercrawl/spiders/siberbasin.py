
import scrapy
import json
from scrapy.crawler import CrawlerProcess
class SiberSpider(scrapy.Spider):
    name = 'siberbasin'
    allowed_domains = ['siberbasin.net']
    start_urls = ['http://siberbasin.net/siber-guvenlik/']
    pagenumber=1
    unique_data=set()
    
          
   

    def parse(self, response):
     div=response.xpath("//*[@class='is-title post-title']")
     
    
     for x in div:
         baslik=x.xpath(".//a/text()").get()
         url=x.xpath(".//a/@href").get()
         
         if baslik not in self.unique_data :
            self.unique_data.add(baslik)
            #burda aynı haberlerin tekrarlanmasını sağlamak için yazılmış bir koddur
            
            yield scrapy.Request(url,callback=self.parse_detail,meta={'baslik':baslik,"url":url})
    
    
    

     next_page='https://siberbasin.net/siber-guvenlik/page/'+str(SiberSpider.pagenumber)+'/'
     if SiberSpider.pagenumber < 10:
         SiberSpider.pagenumber += 1
         Url=response.urljoin(next_page)
         yield scrapy.Request(url=Url, callback=self.parse)

    def parse_detail(self,response):

        baslik=response.meta.get("baslik")
        url=response.meta.get("url")

        metin=response.css(".content-spacious p::text").extract()
        with open("siberbasin.json","a",encoding="UTF-8")as f:
                 f.write(json.dumps({"title":baslik,"url":url,"content":metin,"language":"TR"},indent=2,ensure_ascii=False))
          
proces=CrawlerProcess()
proces.crawl(SiberSpider)
proces.start()              
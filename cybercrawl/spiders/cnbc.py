from ast import Not
import imp
from string import ascii_letters
import scrapy
from scrapy import Request
import json
from scrapy.crawler import CrawlerProcess
class CnbcSpider(scrapy.Spider):
    name = 'cnbc'
    allowed_domains = ['cnbc.com']
    start_urls = ['https://www.cnbc.com/cybersecurity']
    pagenumber=1
    def parse(self, response):
        div=response.xpath("//*[@data-test='Card']/div/div")
        for x in div:
         url=x.xpath("./div[1]//a[contains(@class,'Card-title')]/@href").extract_first()
         tittle=x.xpath("./div[1]//a[contains(@class,'Card-title')]//text()").extract()
         Date=x.xpath("./div[2]/span/text()").extract()
         
         yield response.follow(url,callback=self.parse_detail,meta={"Url":url,"title":tittle,"Date":Date})



        next_page='https://www.cnbc.com/cybersecurity/?page='+str(CnbcSpider.pagenumber)

        if  CnbcSpider.pagenumber <7 :
            #spider sınıfında pagenumber diye bir değişken oluşturuldu
            #1 den başlayan sayfa sayısı 6.sayfaya kadar çalışacak
            #bir sonraki sayfa için bu yöntemi kullanmamdaki sebeb bu web sitesinde sayfa sayısı sonsuz artabiliyor ve hata vermiyor.
            
            CnbcSpider.pagenumber += 1
            link=response.urljoin(next_page)
            yield scrapy.Request(url=link,callback=self.parse)
            
                
        print(CnbcSpider.page)
    def parse_detail(self,response):
        url=response.meta.get("Url")
        title=response.meta.get("title")
        Date=response.meta.get("Date")
        # that method cant get all value because some contect's paragraph attirbuts.
        contect=response.xpath("//*[contains(@class,'ClipPlayer-clipPlayerIntroSummary')]//text()").extract()
        
        if  not contect:
            #boolean methodu contect=False anlamına geliyor . bu bir boş list olduğunu belirtir. 
            #listelerin boş olmasını kontrol etmek için başka kodlarda vardır len(contect) gibi .
            contect=response.xpath("//div[contains(@class,'group')]//p/text()").extract()
        with open("cnbc.json","a",encoding="utf-8")as f:
                 f.write(json.dumps({"title":title,"url":url,"Date":Date,"content":contect,"language":"EN"},indent=2,ensure_ascii=False))   
                 f.close()   
proces=CrawlerProcess()
proces.crawl(CnbcSpider)
proces.start()         
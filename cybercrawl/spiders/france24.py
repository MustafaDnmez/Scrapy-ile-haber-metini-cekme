import scrapy
from scrapy import Request
import json
from scrapy.crawler import CrawlerProcess

class France24Spider(scrapy.Spider):
    name = 'france24'
    allowed_domains = ['france24.com']
    start_urls= ["https://www.france24.com/en/tag/cyber-security/"]


    def parse(self, response):
      div=response.xpath("//section/div/div/div")
      #veriler xpath ile çekilmiştir önce tüm haberleri kapsayan bir pencereyi aldım sonra for döngüsü ile pencere içinde bulunan tüm haber başlıkları url leri çektim.
      for x in div:
        url="https://www.france24.com/"+x.xpath(".//@href").extract_first()
        
        Time=x.xpath(".//div[2]/div/div/time/text()").extract_first().split()
        tittle=x.xpath(".//div[2]/p/text()").extract()
       #css ilede çekebilirsiniz.
        yield Request(url, callback=self.parse_detail,meta={"item":url,"tittle":tittle,"time":Time})
        # meta :spider sözcüğüdür(dict) spider içinde verilerin aktarılmasını sağlıyor.
        
        
       
        
      
      next_page=response.xpath("/html/body/main/div[3]/section/div[4]/ol/li[4]/a/@href").extract_first()
      if next_page is not None:
          #bir sonraki sayfa olduğu sürece bu kod devam edecek eğer son sayfaya ulaşıp bir sonraki sayfa bulunmadığında next_page'in değeri None olarak bu kodlara geçmeyecek 
         link=response.urljoin(next_page)
         yield response.follow(url=link,callback=self.parse)

    #parse_detail fonkisyonu ikinci bir parse olup talep içindeki talep diyebiliriz yukarıda alınan haber sitesinin içine girip metinleri çekme işlemi burada gerçeklşeşir.
    def parse_detail(self,response):
        #def parsin ilettiği veri ve request(talepler) burda kabul edilip çalışacaktır . 
        
        link=response.meta.get("item")
        tittle=response.meta.get("tittle")
        Time=response.meta.get("time")
        #aşağıdaki kod def parse tan gelen Requset url(seçilen haberin urlsi) ile sayfanın içindeki metinleri çekecek
        contect=response.xpath("//div[@class='t-content__body u-clearfix']/p//text()").extract()
        
     
        if len(contect)<1 :
            #eğer boş bir liste gelirse aşağıdaki kod çalışacak.
            contect=response.xpath("//p[@class='t-content__chapo']/text()").extract()

                
            #bazi haberlerin içerik yapıları bir birine benzemiyor olduğu için bir yol daha eklememiz gerekir.
            # bunun için yazdığımız seçicilerle birkaç sayfaya girerek denememizde fayda var
        data=json.dumps({"url":link, "title":tittle,   "Time":Time, "content":contect ,"language":"EN"},indent=2,ensure_ascii=False)
        #burada ben json formatında çıktısını aldım siz istediğiniz çıktılarını almak için dosya uzantısını değiştirebilirsiniz.
        with open ('france24.json','a',encoding="UTF-8") as f:
                f.write(data)
                
     
  
     
#ccrawlprocess ile kodları anaconda veya sanal bir ortam ile terminalsız çalıştırabilir.
proces=CrawlerProcess()
proces.crawl(France24Spider)
proces.start()


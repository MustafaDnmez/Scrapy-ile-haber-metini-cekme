# Scrapy-ile-haber-metini-cekme
Üç farklı haber sitesinden scrapy ile  verileri çekmeyi başaran kodlar bulunmakta . 
kodları incelerken fark edersiniz ben burada meta diye bir özelliği kullandım
meta scrapy içindeki bir sözcük biçiminde verinin iletmesini sağlayan bir özelliktir. bunu kullanmamım sebebi ise 
bir sitenin önce Url'ını çekip sonra o url'ın içindeki metinleri çekmekti bunu yapmak için bazen iki scrapy kullanmamıza gerek 
oluyor veya farklı yöntemle urlleri bir yere kaydedip sonra ordan çekmemizi gerektiriyor. Meta bize bu işlemleri daha kolay bir yolla
gerçekleştirmemizi sağlıyor.

Diğer bir özellik ise spiderleri dosya içinde çalıştırmak . mesela bir anaconda kullanıyorsanız bir spideri çalıştırmak için terminaldan scrapy crawl komutu ile çalıştırmanız gerekecekti ama benim yazdığım bu kodda anacondayi kulllanmada sadece dosyayı çalıştırdığınızda spider çalışır ve verileri çekecektir.

kodlar cybercrawlın içindeki spiders dosyasındadır.

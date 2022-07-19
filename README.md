# Scrapy-ile-haber-metini-cekme
Üç farklı haber sitesinden scrapy ile  verileri çekmeyi başaran kodlar bulunmakta . 
kodları incelerken fark edersiniz ben burada meta diye bir özelliği kullandım
meta scrapy içindeki bir sözcük biçiminde verinin iletmesini sağlayan bir özelliktir. bunu kullanmamım sebebi ise 
bir sitenin önce Url'ını çekip sonra o url'ın içindeki metinleri çekmekti bunu yapmak için bazen iki scrapy kullanmamıza gerek 
oluyor veya farklı yöntemle urlleri bir yere kaydedip sonra ordan çekmemizi gerektiriyor. Meta bize bu işlemleri daha kolay bir yolla
gerçekleştirmemizi sağlıyor.

Diğer bir özellik ise spiderleri dosya içinde çalıştırmak . mesela bir anaconda kullanıyorsanız bir spideri çalıştırmak için terminaldan scrapy crawl komutu ile çalıştırmanız gerekecekti ama benim yazdığım bu kodda anacondayi kulllanmada sadece dosyayı çalıştırdığınızda spider çalışır ve verileri çekecektir.

kodlar cybercrawlın içindeki spiders dosyasındadır.
Sonuç:



"link": "https://www.france24.com//en/tv-shows/tech-24/20210614-the-growing-threat-of-ransomware-attacks",
  "title": [
    "The growing threat of ransomware attacks"
  ],
  "Time": [
    "14/06/2021"
  ],
  "contect": [
    "But first, 99 percent of our telecommunications now transit under our oceans, via underwater cables. Intelligence services around the world are increasingly using these cables to spy on other states, as the NSA allegedly did on German Chancellor Angela Merkel. We take a closer look.",
    "From a major gas pipeline to Florida city's water supply and one of the world's top meat producers, 2021 has seen a sharp rise in ",
    "cyberattacks",
    ", often disrupting sensitive infrastructure. ",
    "Hackers have favoured ransomware attacks, which allow them to gain access to computer systems and disrupt them until they get paid. Our tech editor Peter O'Brien tells us how the practice has grown into a lucrative industry. ",
    "Recently, FBI Director Christopher Wray said the agency was investigating more than 100 different types of ransomware, with many traced back to Russian hackers.  He also compared the current spate of cyberattacks with the challenge once posed by 9/11. The head of France's cybersecurity agency also spoke out, asking French companies to stop paying ransoms. ",
    "To better understand how much of a problem ransomsome attacks have become, we speak to Sébastien Garnault, founder of Paris Cyber Week. ",
    "Plus, in Test 24, we try Technogym MyRun, a treadmill that can be synchronised to your tablet. When linked with its native app or a virtual online trainer, it promises to give other high-end exercise tech devices a run for their money."
  ]

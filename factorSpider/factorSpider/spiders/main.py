from scrapy import cmdline
spider_name = 'detailSpider'
cmdline.execute(['scrapy', 'crawl', spider_name])
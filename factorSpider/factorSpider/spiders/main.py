from scrapy import cmdline
spider_name = 'DetailSpider'
cmdline.execute(['scrapy', 'crawl', spider_name])
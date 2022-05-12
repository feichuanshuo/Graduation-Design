from scrapy import cmdline

# 解除一个注释以启动一个爬虫
# 小区详情爬虫
# spider_name = 'DetailSpider'

# 房天下爬虫
# spider_name = 'FtxSpider'

# 国家数据爬虫
# spider_name = 'GjsjSpider'

# 舆情和房价爬虫
spider_name = 'PoHpSpider'


cmdline.execute(['scrapy', 'crawl', spider_name])
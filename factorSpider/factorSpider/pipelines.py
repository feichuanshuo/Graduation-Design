from scrapy.utils.project import get_project_settings
from factorSpider.items import SupplydataItem,TransactiondataItem,PopulationdataItem
import pymysql


# 房天下管道
class FtxPipeline:
    # def open_spider(self, spider):
    #     self.fp = open('supplyData.json', 'w', encoding='utf-8')
    #
    # def process_item(self, item, spider):
    #     self.fp.write(str(item))
    #     return item
    #
    # def close_spider(self, spider):
    #     self.fp.close()

    def open_spider(self, spider):
        settings = get_project_settings()
        self.host = settings['DB_HOST']
        self.port = settings['DB_PORT']
        self.user = settings['DB_USER']
        self.password = settings['DB_PASSWROD']
        self.name = settings['DB_NAME']
        self.charset = settings['DB_CHARSET']

        self.connect()

    def connect(self):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.name,
            charset=self.charset
        )
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        if spider.name=='FtxSpider':
            sql = ''
            if isinstance(item,SupplydataItem):
                sql = 'insert into supply_data(time,supply_num,supply_area,supply_price,floor_price) values("{}",{},{},{},{})'.format(
                    item['time'],
                    item['supply_num'],
                    item['supply_area'],
                    item['supply_price'],
                    item['floor_price'],
                )
            elif isinstance(item,TransactiondataItem):
                sql ='insert into transaction_data(time,transaction_num,transaction_area,transaction_price,floor_price) values("{}",{},{},{},{})'.format(
                    item['time'],
                    item['transaction_num'],
                    item['transaction_area'],
                    item['transaction_price'],
                    item['floor_price'],
                )
            try:
                # 执行sql语句
                self.cursor.execute(sql)
                # 执行sql语句
                self.conn.commit()
            except:
                # 发生错误时回滚
                self.conn.rollback()

        return item

    # 在爬虫文件执行完之后  执行的方法
    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

# 国家数据管道
class GjsjPipeline:
    def open_spider(self, spider):
        settings = get_project_settings()
        self.host = settings['DB_HOST']
        self.port = settings['DB_PORT']
        self.user = settings['DB_USER']
        self.password = settings['DB_PASSWROD']
        self.name = settings['DB_NAME']
        self.charset = settings['DB_CHARSET']

        self.connect()

    def connect(self):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.name,
            charset=self.charset
        )
        self.cursor = self.conn.cursor()

    def process_item(self,item, spider):
        if spider.name== 'GjsjSpider' :
            if isinstance(item,PopulationdataItem):
                sql = ''
                if item.get('savings_balance',None)==None and item.get('student_num',None)==None:
                    sql = 'insert into population_data(year, population_num, average_wage) values ("{}",{},{})'.format(
                        item['year'],
                        item['population_num'],
                        item['average_wage']
                    )
                elif item.get('savings_balance',None)==None and item.get('student_num',None)!=None:
                    sql = 'update population_data SET student_num = {} where year="{}"'.format(
                        item['student_num'],
                        item['year']
                    )
                elif item.get('savings_balance',None)!=None and item.get('student_num',None)==None:
                    sql = 'update population_data SET savings_balance = {} where year="{}"'.format(
                        item['savings_balance'],
                        item['year']
                    )
                try:
                    # 执行sql语句
                    self.cursor.execute(sql)
                    # 执行sql语句
                    self.conn.commit()
                except:
                    # 发生错误时回滚
                    self.conn.rollback()

        return item
    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

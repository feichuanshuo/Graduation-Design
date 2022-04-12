from scrapy.utils.project import get_project_settings
from factorSpider.items import SupplydataItem,TransactiondataItem,PopulationdataItem,EnvironmentdataItem,DetailItem
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
            sql = ''
            if isinstance(item,PopulationdataItem):
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
            elif isinstance(item,EnvironmentdataItem):
                if item.get('traffic_noise',None)==None and item.get('ambient_noise',None)==None:
                    sql = 'insert into environment_data(year,hospital_num,doctor_num,cinema_num) values ("{}",{},{},{}) '.format(
                        item['year'],
                        item['hospital_num'],
                        item['doctor_num'],
                        item['cinema_num']
                    )
                elif item.get('traffic_noise',None)!=None and item.get('ambient_noise',None)!=None:
                    sql = 'update environment_data SET traffic_noise={},ambient_noise={} where year="{}"'.format(
                        item['traffic_noise'],
                        item['ambient_noise'],
                        item['year'],
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

# 小区详情管道
class DetailPipeline:
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
        if spider.name== 'DetailSpider' :
            sql = ''
            if isinstance(item,DetailItem):
                sql = 'insert into detail_data(name,price,address,plotRatio,greeningRate,busStop,subwayStations,kindergarten,primarySchool,middleSchool,hospital,CAhospital,shoppingMall,supermarket,park) values ("{}",{},"{}",{},{},{},{},{},{},{},{},{},{},{},{})'.format(
                    item['name'],
                    item['price'],
                    item['address'],
                    item['plotRatio'],
                    item['greeningRate'],
                    item['busStop'],
                    item['subwayStations'],
                    item['kindergarten'],
                    item['primarySchool'],
                    item['middleSchool'],
                    item['hospital'],
                    item['CAhospital'],
                    item['shoppingMall'],
                    item['supermarket'],
                    item['park']
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
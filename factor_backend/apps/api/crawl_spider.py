# from flask import Blueprint,request
# import sys
# from libs.response import Success,ServerError
#
# api = Blueprint('crawl_spider',__name__,url_prefix='/crawl_spider')
# # 爬虫文件列表
# spiderList = ['FtxSpider','GjsjSpider']
#
# @api.route('',methods=['GET'])
# def crawl_spider():
#     return Success(spiderList)
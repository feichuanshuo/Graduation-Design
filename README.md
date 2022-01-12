# Graduation-Design
基于爬虫技术的西安房地产发展影响因素数据库设计

## 一、项目简介

- 分析、识别西安市房地产发展的供需影响因素（宏观因素和微观因素）
- 设计爬虫软件获取房地产发展的影响因素数据
- 构建房地产发展的影响因素数据库
- 基于上述数据的人工智能应答系统设计

## 二、部署步骤

## 三、目录结构描述

```
factor_ui				前端，数据可视化
factorSpider			爬虫
```

## 四、项目进度

- #### 爬虫

  宏观：国家政策（主席）方面的影响因素经济（国务院）文化

  中观：西安在西部地区的影响因素，人（进入人口）、财（投资公司）、物（科技园）

  微观：

   	供给、成交（拿地的数量和价格）

  ```
  房天下：https://fdc.fang.com/data/land/land_xa.htm
  url:
  https://fdc.fang.com/data/ajax/LandPicTable.aspxDataType=1&LandType=&Locus=610100&Time=m&BeginTime=2021.05&EndTime=2021.10
  ```

  ​	西安对医疗、交通和教育的投资、需求（产业和工资（私营企业））、学历结构、平均工作年龄

  ```
  国家数据：https://data.stats.gov.cn/
  
  人口和就业（年末总人口(万人)、在岗职工平均工资(元)）
  url:'https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=csnd&rowcode=zb&colcode=sj&wds=[{"wdcode":"reg","valuecode":"610100"}]&dfwds=[{"wdcode":"zb","valuecode":"A02"},{"wdcode":"sj","valuecode":"LAST20"}]&k1='+时间戳+"&h=1
  
  教育、卫生、文化（普通本专科学生(万人)、医院数(个)、执业(助理)医师数(万人)、剧场、影剧院数(个)）
  url:'https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=csnd&rowcode=zb&colcode=sj&wds=[{"wdcode":"reg","valuecode":"610100"}]&dfwds=[{"wdcode":"zb","valuecode":"A08"},{"wdcode":"sj","valuecode":"LAST20"}]&k1='+时间戳+"&h=1"
  
  财政和金融
  url:'https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=csnd&rowcode=zb&colcode=sj&wds=[{"wdcode":"reg","valuecode":"610100"}]&dfwds=[{"wdcode":"zb","valuecode":"A04"},{"wdcode":"sj","valuecode":"LAST20"}]&k1='+时间戳+"&h=1",
          
  运输和邮电（邮政局(所)数(处)、固定电话用户数(万户)）
  url:
  
  噪声监测（道路交通等效声级dB(A)、环境噪声等效声级dB(A)）
  url:
  房地产舆情 数据源： 百度指数，天涯论坛，房天下，安居客
  ```

  

- #### 数据库

  土地供应数据--supply_data

  ```
  --time      	    	月份
  --supply_num			供应宗数(块) 	
  --supply_area			供应面积(㎡) 	
  --supply_price			供应均价(元/㎡)
  --floor_price			楼面价(元/㎡)
  ```

  土地成交数据--transaction_data

  ```
  --time					月份 
  --transaction_num		成交宗数(块)	
  --transaction_area		成交面积(㎡) 	
  --transaction_price		成交均价(元/㎡)
  --floor_price			楼面价(元/㎡)
  ```

  人口数据--population_data

  ```
  --year					年份
  --population_num		年末总人口(万人)
  --average_wage			在岗职工平均工资(元)
  --savings_balance		城乡居民储蓄年末余额(亿元)
  --student_num			普通本专科学生(万人)
  ```

- #### 前端

- #### 后端

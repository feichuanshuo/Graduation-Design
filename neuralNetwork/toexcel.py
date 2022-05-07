import pymysql
import pandas as pd


if __name__ == '__main__':
    # 打开数据库连接
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='root',
                         database='influence_factor')

    dataList = []

    dataLen = 0

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    sql = "SELECT * FROM detail_data WHERE price!=0 and plotRatio!=0 and greeningRate!=0"

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        dataLen = len(results)
        for row in results:
            rowdata = []
            rowdata.append(row[0])
            rowdata.append(row[1])
            rowdata.append(row[3])
            rowdata.append(row[4])
            rowdata.append(row[5])
            rowdata.append(row[6])
            rowdata.append(row[7])
            rowdata.append(row[8])
            rowdata.append(row[9])
            rowdata.append(row[10])
            rowdata.append(row[12])
            rowdata.append(row[13])
            rowdata.append(row[14])
            dataList.append(rowdata)

    except:
        print("Error: unable to fetch data")

    # 关闭数据库连接
    db.close()

    pdxy = pd.DataFrame(dataList,columns=['小区名','政府参考价','容积率','绿化率','公交站数','地铁站数','幼儿园数','小学数','中学数','医院数','购物中心数','超市数','公园数'])
    pdxy.to_excel('data.xlsx',index=False)
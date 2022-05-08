import pymysql
import torch
from torch import nn, optim
import matplotlib.pyplot as plt


class Net(torch.nn.Module):  
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Linear(12, 16),
            nn.ReLU(),
            nn.Linear(16, 32),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(32, 8),
            nn.ReLU(),
            nn.Linear(8, 1),
        )

    def forward(self, x):
        x = self.conv1(x)
        return x

# 返回预估价
def get_estimated_data(data):
    model = Net()  # 把网络模型赋值给model，并且把模型放到GPU上运行
    model.load_state_dict(torch.load('libs/neuralNetwork/dl.pth'))  # 加载模型参数
    model.eval()
    estimated_data = model(torch.tensor(data, dtype=torch.float32)).item()
    return round(estimated_data,2)

def normalize(x):
    min = torch.min(x)
    max = torch.max(x)
    return (x - min) / (max - min)


if __name__ == '__main__' :
    # 打开数据库连接
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='root',
                         database='influence_factor')
    dataList = []

    dataLen = 0

    lossMin = float("inf")
    parameter = None

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    sql = "SELECT * FROM detail_data WHERE price!=0 and plotRatio!=0 and greeningRate!=0 and emotionIndex is not null"

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        dataLen = len(results)
        for row in results:
            rowdata = []
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
            rowdata.append(row[17])
            dataList.append(rowdata)



    except:
        print("Error: unable to fetch data")

    # 关闭数据库连接
    db.close()

    print(dataList)

    data = torch.tensor(dataList)
    # 训练数据
    xtrain = data[0:-100, 1:]
    ytrain = data[0:-100, [0]]
    # 测试数据
    xtest = data[-100:, 1:]
    ytest = data[-100:, [0]]

    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')  # 定义一个运算设备，如果电脑有GPU就用GPU运算，如果没有就用CPU运算
    model = Net().to(device)  # 把网络模型赋值给model，并且把模型放到GPU上运行
    criteon = nn.MSELoss().to(device)  # 定义损失函数类型，并且把它放到GPU上运行
    optimizer = optim.Adam(model.parameters(), lr=0.0005)  # 定义优化方式，梯度下降算法参数调整
    trainlosslist = []  # 定义在训练时,累计每个epoch的loss值存储数组
    testlosslist = []  # 定义在测试时,累计每个epoch的loss值存储数组
    plt.ion()  # 开启plt画图，动态图模式

    for epoch in range(200000):  # 循环训练200次
        model.train()  # 切换到训练模式
        xtrain = xtrain.to(device)  # 把训练x放到GPU上执行
        ytrain = ytrain.to(device)  # 把训练y放到GPU上执行
        logits = model(xtrain)  # 通过网络模型的运算，得到预测值
        loss = criteon(logits, ytrain) / dataLen # 通过损失函数的运算，得到损失值
        optimizer.zero_grad()  # 清空w，b的导数
        loss.backward()  # 每次网络的W,B全部自动求导计算出导数
        optimizer.step()  # 根据你定义的梯度下降规则来更新每层网络的W和b
        trainlosslist.append(loss.item())  # 把这一轮训练计算得出的loss值放入trainlosslist数组
        model.eval()  # 切换到测试模式
        with torch.no_grad():  # 测试模式，不需要任何w，b的导数值
            xtest = xtest.to(device)  # 把测试x放到GPU上执行
            ytest = ytest.to(device)  # 把测试y放到GPU上执行
            logits = model(xtest)  # 通过网络模型的运算，得到预测值
            testloss = criteon(logits, ytest) / dataLen# 通过损失函数的运算，得到损失值
            testlosslist.append(testloss.item())  # 把这一轮测试计算得出的loss值放入testlosslist数组
            print(testloss.item())
            if testloss.item() < lossMin :
                lossMin = testloss.item()
                parameter = model.state_dict()
                torch.save(parameter, 'dl.pth')

    #     plt.cla()  # 因为是动态图，所以先擦除上一张图
    #     l1, = plt.plot(trainlosslist)  # 把每一轮的训练loss值画出来
    #     l2, = plt.plot(testlosslist)  # 把每一轮的测试loss值画出来
    #     plt.legend([l1, l2], ['tranloss', 'testloss'], loc='best')  # 显示图例
    #     plt.xlabel('epochs')  # 画的图x轴，标注epochs字样
    #     plt.pause(0.02)  # 暂停0.2秒，以免画的太快感觉不到图在动
    #     plt.ioff()  # 结束动态图模式
    # plt.show()  # 最终显示图片
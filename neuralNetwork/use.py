import torch
from main import Net


if __name__ == '__main__':
    model = Net() # 把网络模型赋值给model，并且把模型放到GPU上运行

    model.load_state_dict(torch.load('dl.pth'))  # 加载模型参数
    model.eval()
    xlist = torch.tensor([[2,30,5,62,107,31,12,9,34,957,11]], dtype=torch.float32)

    print(model(xlist).item())
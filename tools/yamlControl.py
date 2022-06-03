import yaml

def get_yaml_data(fileDir):
    resList = []#存放结果[(请求1，期望响应1)，(请求2，期望响应1)]
    #1 读取yaml文件操作 --从磁盘读取到内存里
    fo = open(fileDir, 'r',encoding="utf-8")#PEP8编码规则
    #2 使用yaml方法获取数据
    res = yaml.load(fo,Loader=yaml.FullLoader)
    # print(str(type(res)))
    fo.close()
    #具体返回什么类型，根据需求来定
    info = res[0]
    # print(res[0])
    del res[0] #删除第一个
    for one in res:
        resList.append((one['data'],one['resp']))
        # print(one)
    return res
if __name__ == '__main__':
    res = get_yaml_data('../data/login.yaml')
    # print(res)

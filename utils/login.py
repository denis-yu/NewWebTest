# author Denis Yu

import requests
import hashlib
import pprint
#封装一个MD5加密

def get_md5(psw):
    """
    params: psw
    return:返回md5加密值
    """
    # 实例化一个md5加密函数
    md5 = hashlib.md5()
    # 调用加密方法加密
    md5.update(psw.encode("utf-8"))
    return md5.hexdigest()
class Login:
    def login(self,data,mode=True):
        # 路径
        url='http://121.41.14.39:9097/api/loginS'
        # url = 'http://121.41.14.39:9097'
        #字典名【键名】=新的值   字典修改值操作
        data["password"]=get_md5(data["password"])
        #参数
        payload = data
        """
        data - 一般表格格式
        json - json
        files - 文件上传接口
        params - 参数会放到url?a=1&b=2
        """
        #   请求
        resp = requests.post(url,json=payload)
        # return resp.text  # json字符串
        if mode: # 获取token
            return  resp.json()["token"] #返回是字典类型
        else: # 获取相应数据
            return  resp.json() #返回是字典类型

if __name__ == '__main__':
    res = Login().login ({"username":"20154084","password":"123456"})
    print(res)
    # print(get_md5("123456"))
    pprint.pprint(res)
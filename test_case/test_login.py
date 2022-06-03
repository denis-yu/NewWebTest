
from tools.yamlControl import get_yaml_data
from utils import login
import pytest
import allure,os

from utils.login import Login


class TestLogin:
    #测试方法
    # @pytest.mark.parametrize('inBody,expData',get_yaml_data('../data/login.yaml'))#数据驱动方法

    # def test_login(self,inBody,expData):
    #     #调用业务代码
    #     print(str(type(inBody)))
    #     print(str(type(expData)))
    #     res = Login().login(inBody, False)
    #     print(res)
    #     assert res['message'] == expData['message']#断言
#执行用例
    # 1- 获取用例数据
    res = get_yaml_data('../data/login.yaml')[0]
    print(res)
    print(str(type(res['data'])))
    # 2-调用接口方法
    respData = Login().login(res['data'], False)
    print(respData)
    a = respData['message']
    b = res['resp']['message']
    # 3-断言
    if a == b:
        print('---用例通过---')
    else:
        print('---用例不通过---')

# if __name__ == '__main__':
    # pytest.main(["test_login.py","-s","alluredir","../report/tmp"]) #生成报告的所需的文件
    # pytest.main(["test_login.py", "-s"])
    # os.system("allure serve ../report/tmp") #使用allure生成并打开报告
"""
引入测试框架：pytest
报告：allure+log
持续集成：jenkins+gitlab+邮件插件
部署持续环境： docker
 
"""
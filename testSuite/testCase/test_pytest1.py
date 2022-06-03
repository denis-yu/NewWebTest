
import pytest
# import logging
import allure

# logging.basicConfig(level=logging.DEBUG)

@pytest.fixture(scope="module", autouse=True)
def start(request):
    print("\n----开始执行module------")
    print('module : %s' % request.module.__name__)
    print('------启动浏览器-------')
    yield
    print("------结束测试 end!----------")


@pytest.fixture(scope="function", autouse=True)
def open_home(request):
    print("function:%s \n--回到首页--" % request.function.__name__)

@allure.feature('test_module_01')
def test_01():
    # log = logging.getLogger('test_01')
    # log.debug('----用例01-----')
    print('----用例01-----')

@allure.feature('test_module_02')
def test_02():
    # log = logging.getLogger('test_02')
    # log.debug('----用例02-----')
    print('----用例02-----')

if __name__ == '__main__':
    print('----开始生成结果-----')
    pytest.main(['-s', '-q', '--alluredir', './report/xml'])
    print('----生成结果-----')
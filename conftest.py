#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
import allure
import os
import uuid

sys.path.append('.')
__author__ = 'denis.yu@suryani.cn'

import pytest
from py._xmlgen import html
from selenium import webdriver

driver = None


@pytest.fixture(scope='session', autouse=True)
def drivers(request):
    global driver
    if driver is None:
        driver = webdriver.Chrome()
        driver.maximize_window()

    def fn():
        driver.quit()

    request.addfinalizer(fn)
    return driver


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        #判断用例是否失败或者xfail跳过的测试
        if (report.skipped and xfail) or (report.failed and not xfail):
        	#获取测试用例代码中webDriver参数来获取浏览器进行抓屏
            for i in item.funcargs:
                if isinstance(item.funcargs[i], driver):
                	#截图
                    save_capture(item.funcargs[i], "异常截图")
                    pass
                pass
            pass
        report.extra = extra


# @pytest.mark.optionalhook
# def pytest_html_results_table_header(cells):
#     cells.insert(1, html.th('用例名称'))
#     cells.insert(2, html.th('Test_nodeid'))
#     cells.pop(2)
#
#
# @pytest.mark.optionalhook
# def pytest_html_results_table_row(report, cells):
#     cells.insert(1, html.td(report.description))
#     cells.insert(2, html.td(report.nodeid))
#     cells.pop(2)
#
#
# @pytest.mark.optionalhook
# def pytest_html_results_table_html(report, data):
#     if report.passed:
#         del data[:]
#         data.append(html.div('通过的用例未捕获日志输出.', class_='empty log'))


def _capture_screenshot(driver):
    # fileName = config.screenPath + '/' + str(uuid.uuid1()) + '.png'
    fileName = '/Users/denisyu/workplace/test/NewWebTest/screenshots/' + str(uuid.uuid1()) + '.png'
    driver.get_screenshot_as_file(fileName)
    return fileName


def save_capture(driver, name: str):
    fileName = _capture_screenshot(driver)
    if os.path.exists(fileName):
        allure.attach.file(fileName,
                           attachment_type=allure.attachment_type.PNG, name=name)
        pass
    pass

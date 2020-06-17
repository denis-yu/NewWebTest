#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = 'Denis Yu in HeallthPocket XM'


sys.path.append('.')
import os
from selenium.webdriver.common.by import By

# 项目目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 配置文件
INI_PATH = os.path.join(BASE_DIR, 'config', 'config.ini')

# 页面元素目录
ELEMENT_PATH = os.path.join(BASE_DIR, 'page_element')

# 日志目录
LOG_PATH = os.path.join(BASE_DIR, 'logs')

# 报告目录
REPORT_PATH = os.path.join(BASE_DIR, 'report', 'report.html')

# 元素定位的类型
LOCATE_MODE = {
    'css': By.CSS_SELECTOR,
    'xpath': By.XPATH,
    'name': By.NAME,
    'id': By.ID,
    'class': By.CLASS_NAME,
    'link': By.LINK_TEXT
}

# 邮件信息
EMAIL_INFO = {
    'username': '761539054@qq.com',  # 切换成你自己的地址
    'password': 'xqaitysdrakxbehi',
    'smtp_host': 'smtp.qq.com',
    'smtp_port': 465
}

# 收件人
ADDRESSEE = [
    'denis.yu@suryani.cn',
]

if __name__ == '__main__':
    print(BASE_DIR)
    print(INI_PATH)
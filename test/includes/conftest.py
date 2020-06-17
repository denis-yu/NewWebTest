import pytest
from selenium import webdriver



def open_url():
    # 前置
    driver = webdriver.Chrome()
    driver.get("https://sunmaker.medicare.healthinsurance.com") #url为链接地址
    yield driver    #yield之前代码是前置，之后的代码就是后置。
    # 后置
    driver.quit()

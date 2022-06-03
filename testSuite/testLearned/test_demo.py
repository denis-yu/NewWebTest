from selenium import webdriver
import time

def test_case(browser):
    browser.get("https://www.baidu.com/")
    time.sleep(2)
    t = browser.title
    assert t=="software test"
    print(t)
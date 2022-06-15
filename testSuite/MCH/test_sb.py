# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestMedicare():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_medicare(self):
        self.driver.get("https://pengujian.healthpocket.com/")
        self.driver.set_window_size(1246, 796)
        self.driver.find_element(By.ID, "location").click()
        self.driver.find_element(By.ID, "location").send_keys("60601")
        self.driver.find_element(By.LINK_TEXT, "60601 - Cook County, IL").click()
        self.driver.find_element(By.ID, "planTypeDropdown").click()
        self.driver.find_element(By.LINK_TEXT, "Small Business Insurance").click()
        self.driver.find_element(By.ID, "findPlans").click()
        self.driver.find_element(By.CSS_SELECTOR, ".js-filter-plan-type-toggle").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 "#js-filter-plan-type-popover .l-em-list__item:nth-child(1) .btn").click()
        self.driver.find_element(By.CSS_SELECTOR, "#js-filter-plan-type-popover .c-census-popover__button").click()
        self.driver.find_element(By.LINK_TEXT, "Select").click()
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".c-plan-apply_h1").text == "Aetna Health Maintenance Organization"

# -- coding: utf-8 --
# @Time : 6/4/22 3:22 PM
# @Project : NewWebTest
# @Author : Denis Yu
# @File : test_sb.py
# @Software: PyCharm
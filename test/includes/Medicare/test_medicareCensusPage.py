from startDriver import startDriver
import pytest
import allure
# from selenium import webdriver
import os, time, random
from selenium.webdriver.common.by import By
# import sys
# sys.path.append(os.getcwd())
# sys.path.append(os.getcwd()+"../startDriver.py")
# print(os.getcwd())


class TestMedicareCensusPage(startDriver):

    # def get_start_url(self):
    #     self.driver.get("https://sunmaker.medicare.healthinsurance.com")

    def get_zip(self):
        zip = "30301"
        return zip
    # def get_guote(self):

    @allure.story('Census Page')
    def test_medicareCensus(self):

        with allure.step(title='open census page'):

            # Step # | name | target | value

            # 1 | open | / |

            self.driver.get("https://sunmaker.medicare.healthinsurance.com")
            # self.get_start_url()
            # 2 | setWindowSize | 1440x900 |
            # self.set_window_size(1440, 900)
            # 3 | click | linkText=Census |
            # self.driver.find_element(By.LINK_TEXT, "Census").click()
            # 4 | click | name=census.location.zip |
            self.driver.implicitly_wait(60)
            self.driver.find_element(By.NAME, "census.location.zip").click()
            # 5 | type | name=census.location.zip | 30301
            time.sleep(5)
            self.driver.find_element(By.NAME, "census.location.zip").send_keys(self.get_zip())
            # 6 | click | xpath=//div[@id='__next']/div[2]/div/div/div[2]/div |
            self.driver.implicitly_wait(60)
            time.sleep(5)

if __name__ == '__main__':
    new_medicare_census = TestMedicareCensusPage()
    new_medicare_census.test_medicareCensus()
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    pytest.main("-s -q test_medicareCensusPage.py  --alluredir result".format(now))


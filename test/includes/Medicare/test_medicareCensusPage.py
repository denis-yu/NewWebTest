from startDriver import startDriver
import pytest
import allure
# from selenium import webdriver
import os, time, random
# import sys
# sys.path.append(os.getcwd())
# sys.path.append(os.getcwd()+"../startDriver.py")
# print(os.getcwd())


class Test_medicareCensusPage(startDriver):
    def __init__(self):
        newtest = startDriver("chrome")

    def get_start_url(self):
        self.driver.get("https://sunmaker.medicare.healthinsurance.com")

    def get_zip(self):
        zip = "30301"
    # def get_guote(self):

@allure.story('Census Page')
def test_medicareCensus():
    new_medicare_census = test_medicareCensusPage()
    with allure.step(title='open census page'):

        # Step # | name | target | value

        # 1 | open | / |

        # self.driver.get("https://sunmaker.medicare.healthinsurance.com")
        new_medicare_census.get_start_url()
        # 2 | setWindowSize | 1440x900 |
        new_medicare_census.driver.set_window_size(1440, 900)
        # 3 | click | linkText=Census |
        # self.driver.find_element(By.LINK_TEXT, "Census").click()
        # 4 | click | name=census.location.zip |
        self.driver.implicitly_wait(60)
        self.driver.find_element(By.NAME, "census.location.zip").click()
        # 5 | type | name=census.location.zip | 30301
        time.sleep(5)
        self.driver.find_element(By.NAME, "census.location.zip").send_keys("30301")
        # 6 | click | xpath=//div[@id='__next']/div[2]/div/div/div[2]/div |
        self.driver.implicitly_wait(60)
        time.sleep(5)

if __name__ == '__main__':
    test_medicareCensus()
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    pytest.main("-s -q test_comparePlanDetail.py  --alluredir result".format(now))


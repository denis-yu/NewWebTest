#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
import time
import allure

sys.path.append('.')
__author__ = 'Denis yu'

import re
import pytest
from tools.logger import log
from common.readconfig import ini
from page_object.medicare_censuspage import CensusPage

@allure.story('visit census page')
class TestCensus:
    # @pytest.fixture(scope='function', autouse=True)

    with allure.step(title='open census page'):
        def test_openmedicaresite(self, drivers):
            """open medicare site"""
            census = CensusPage(drivers)
            census.get_url(ini.url)
    with allure.step(title='open medicare quote page'):
        def test_medicarecensus(self, drivers):
            """get medicare quote"""
            census = CensusPage(drivers)
            # census.get_url(ini.url)
            census.input_zipcode("30301")
            time.sleep(10)
            census.get_quote
            print("get medicare quote successfully")



if __name__ == '__main__':
    # pytest.main(['test/Medicare/test_census.py'])
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    pytest.main("-s -q test/Medicare/test_census.py  --alluredir results".format(now))


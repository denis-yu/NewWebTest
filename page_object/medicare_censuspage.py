#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')


from page.webpage import WebPage, sleep
from common.readelement import Element

census = Element('medicarecensus')


class CensusPage(WebPage):
    def input_zipcode(self, content):
        """input zipcode"""
        self.input_text(census['zipCode'], txt=content)
        sleep()

    @property


    def get_quote(self):
        """get medicare quote"""
        self.is_click(census['quoteButton'])


if __name__ == '__main__':
    pass
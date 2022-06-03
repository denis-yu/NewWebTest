#!/usr/bin/env python
# -*- coding: utf-8 -*-
from code.cau import cau
class Test_cover:
    def test_add(self):
        a=cau(1,2,3)
        assert a==3

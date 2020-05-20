import numpy as np
import pandas as pd


class TestCase():
    def __init__(self, filename):
        self.df_obj = pd.read_csv(filename)

    def write(self, i, j, value):
        self.df_obj.iloc[i, j] = value


if __name__ == '__main__':
    filename = '../../data/comparePlanDetails.csv'
    t = TestCase(filename)

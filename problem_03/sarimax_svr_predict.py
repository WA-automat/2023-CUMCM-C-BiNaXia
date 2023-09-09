import math
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.svm import SVR
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import random

categoryFile = '../data/2023年6月24-30可售单品信息.csv'
file1 = '../附件1-蔬菜品类的商品信息.csv'
file2 = '../附件2-销售流水明细数据.csv'
file3 = '../附件3-蔬菜类商品批发价格.csv'
file4 = '../附件4-蔬菜类商品的近期损耗率.csv'

categoryData = pd.read_csv(categoryFile)
df2 = pd.read_csv(file2)

new_df2 = pd.DataFrame(columns=df2.columns)


def prework():
    for index, row in df2.iterrows():
        if index % 10000 == 0:
            print(index)
        if int(row['单品编码']) in categoryData['单品编码'].tolist():
            new_df2.loc[len(new_df2)] = row
    new_df2.to_csv('../2023年6月24-30可售单品销售流水明细数据.csv')


if __name__ == '__main__':
    prework()

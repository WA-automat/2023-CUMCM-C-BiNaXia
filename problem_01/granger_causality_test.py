import pandas as pd
from statsmodels.tsa.stattools import grangercausalitytests

df = pd.read_csv('../data/各蔬菜品类对应日期的销售量.csv')


def get_cate_name_by_code(code):
    data = pd.read_csv('../附件1-蔬菜品类的商品信息.csv')
    for index, row in data.iterrows():
        if str(row['分类编码']) == str(code):
            return row['分类名称']


def granger_causality_test(code1, code2):
    return grangercausalitytests(df[[code1, code2]], maxlag=1)


if __name__ == '__main__':
    cate_codes = ['1011010201', '1011010402', '1011010501', '1011010504', '1011010801']

    for code1 in cate_codes:
        for code2 in cate_codes:
            if code1 != code2:
                print(get_cate_name_by_code(code1) + '与' + get_cate_name_by_code(code2) + ':')
                print(granger_causality_test(code1, code2))
                print("===========================================")

import numpy as np
import pandas as pd
from statsmodels.tsa.vector_ar.vecm import coint_johansen


def get_cate_name_by_code(code):
    data = pd.read_csv('../附件1-蔬菜品类的商品信息.csv')
    for index, row in data.iterrows():
        if str(row['分类编码']) == code:
            return row['分类名称']


def cointgration_test(data1, data2):
    """
    进行两个序列数据的协整检验
    :param data1: 序列数据1
    :param data2: 序列数据2
    :return: 检验结果res(res.lr1[0]<res.lr2[0]则存在协整关系)
    """
    data1 = np.asarray(data1)
    data2 = np.asarray(data2)
    return coint_johansen(np.column_stack((data1, data2)), det_order=0, k_ar_diff=0)


if __name__ == '__main__':
    cate_codes = ['1011010201', '1011010402', '1011010501', '1011010504', '1011010801']
    df = pd.read_csv('../data/各蔬菜品类对应日期的销售量.csv')
    for code1 in cate_codes:
        for code2 in cate_codes:
            if code1 == code2:
                continue
            res = cointgration_test(df[code1], df[code2])
            num_of_coint = np.sum(res.lr1 > res.cvt[:,1]) # 95% 置信水平
            if num_of_coint > 0:
                print(get_cate_name_by_code(code1) + '与' + get_cate_name_by_code(code2) + '存在协整关系')
                print('=================================================')
            else:
                print(get_cate_name_by_code(code1) + '与' + get_cate_name_by_code(code2) + '不存在协整关系')
                print('=================================================')

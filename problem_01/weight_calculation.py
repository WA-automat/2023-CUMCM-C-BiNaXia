import numpy as np
import pandas as pd

file1 = '../附件1-蔬菜品类的商品信息.csv'
file2 = '../附件2-销售流水明细数据.csv'
file3 = '../附件3-蔬菜类商品批发价格.csv'


def get_item_msg_by_code(code):
    data = pd.read_csv(file1)
    for index, row in data.iterrows():
        if str(row['单品编码']) == str(code):
            return {
                '单品编码': row['单品编码'],
                '单品名称': row['单品名称'],
                '分类编码': row['分类编码'],
                '分类名称': row['分类名称']
            }


def get_code_weight():
    codeTable = pd.read_csv(file1)
    data = pd.read_csv(file2)
    cost = pd.read_csv(file3)
    mp = {}
    ans = {}
    for index, row in data.iterrows():
        mp[str(row['单品编码'])] = 0
        tmp = get_item_msg_by_code(str(row['单品编码']))
        ans[tmp['分类编码']] = 0
    print('开始计算贡献率')
    for index, row in data.iterrows():
        tmpPrice = row['销量(千克)'] * \
                   (row['销售单价(元/千克)'] -
                    cost[np.logical_and(str(cost['单品编码']) == str(row['单品编码']),
                                        cost['日期'] == row['销售日期'])])
        mp[str(row['单品编码'])] += tmpPrice
        tmp = get_item_msg_by_code(str(row['单品编码']))
        ans[tmp['分类编码']] += tmpPrice
    df = pd.DataFrame(index=['单品编码', '分类编码', '贡献率'])
    for index, row in codeTable.iterrows():
        tmp = get_item_msg_by_code(str(row['单品编码']))
        df.loc[len(df)] = [tmp['单品编码'], tmp['分类编码'], mp[str(row['单品编码'])] / ans[tmp['分类编码']]]
    print('贡献率计算完成')
    df.to_csv('../data/各单品对应品类的贡献率.csv')


if __name__ == '__main__':
    get_code_weight()

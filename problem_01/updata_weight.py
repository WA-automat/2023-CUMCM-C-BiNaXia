import pandas as pd
import math


def get_item_msg_by_code(code):
    data = pd.read_csv('../附件1-蔬菜品类的商品信息.csv')
    for index, row in data.iterrows():
        if str(row['单品编码']) == str(code):
            return {
                '单品编码': row['单品编码'],
                '单品名称': row['单品名称'],
                '分类编码': row['分类编码'],
                '分类名称': row['分类名称']
            }


def get_cate_name_by_code(code):
    data = pd.read_csv('../附件1-蔬菜品类的商品信息.csv')
    for index, row in data.iterrows():
        if str(row['分类编码']) == str(code):
            return row['分类名称']


def update_weight():
    df = pd.read_csv('../data/各单品对应品类的贡献率.csv')
    cate_weight = {}
    for idx, row in df.iterrows():
        if str(int(row['分类编码'])) not in cate_weight.keys():
            cate_weight[str(int(row['分类编码']))] = 0
        cate_weight[str(int(row['分类编码']))] += math.exp(row['贡献率'])
    res_df = {}
    for idx, row in df.iterrows():
        tmp = {
            '贡献率': math.exp(row['贡献率']) / cate_weight[str(int(row['分类编码']))]
        }
        res_df[str(int(row['单品编码']))] = tmp

    dfx = pd.DataFrame(columns=['单品编码', '分类编码', '贡献率'])
    for index, row in df.iterrows():
        tmp = get_item_msg_by_code(str(int(row['单品编码'])))
        dfx.loc[len(dfx)] = [str(tmp['单品编码']), str(tmp['分类编码']), res_df[str(tmp['单品编码'])]['贡献率']]
    # print(dfx)
    dfx.to_csv('../data/各单品对应品类的贡献率(标准化).csv')


if __name__ == '__main__':
    update_weight()

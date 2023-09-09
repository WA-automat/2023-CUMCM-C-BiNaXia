import numpy as np
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

file1 = '../附件1-蔬菜品类的商品信息.csv'
file2 = '../附件2-销售流水明细数据.csv'
file3 = '../附件3-蔬菜类商品批发价格.csv'
file4 = '../data/各单品对应品类的贡献率(标准化).csv'
dictTable = {}

categoryCodes = [1011010101, 1011010201, 1011010402, 1011010501, 1011010504, 1011010801]


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


def prework():
    codeTable = pd.read_csv(file1)
    for index, row in codeTable.iterrows():
        tmp = get_item_msg_by_code(str(row['单品编码']))
        dictTable[str(tmp['单品编码'])] = tmp


def price_cost_calculation():
    prework()
    print(dictTable)
    priceData = pd.read_csv(file2)
    costData = pd.read_csv(file3)
    weightData = pd.read_csv(file4)
    priceData['销售日期'] = pd.to_datetime(priceData['销售日期'])
    costData['日期'] = pd.to_datetime(costData['日期'])
    times = priceData['销售日期'].unique()
    res_df = pd.DataFrame(columns=['时间', '分类编码', '加权售价', '加权成本'])
    for time in times:
        print(time)
        datePriceData = priceData[priceData['销售日期'] == time]
        dateCostData = costData[costData['日期'] == time]
        for index, row in datePriceData.iterrows():
            # print(dictTable[str(row['单品编码'])]['分类编码'])
            datePriceData.loc[index, '品类'] = str(dictTable[str(row['单品编码'])]['分类编码'])

        for index, row in dateCostData.iterrows():
            # print(dictTable[str(row['单品编码'])]['分类编码'])
            dateCostData.loc[index, '品类'] = str(dictTable[str(row['单品编码'])]['分类编码'])

        for categoryCode in categoryCodes:
            itemPriceData = datePriceData[datePriceData['品类'] == str(categoryCode)]
            itemCostData = dateCostData[dateCostData['品类'] == str(categoryCode)]
            itemPriceSet = itemPriceData['单品编码']
            itemCostSet = itemCostData['单品编码']

            # 求权重和（分母）
            priceWeightSum = 0
            for item in itemPriceSet:
                priceWeightSum += weightData[weightData['单品编码'] == item]['贡献率'].values[0]
            costWeightSum = 0
            for item in itemCostSet:
                costWeightSum += weightData[weightData['单品编码'] == item]['贡献率'].values[0]

            # 求权重*价格
            priceSum = 0
            for index, row in itemPriceData.iterrows():
                weight = weightData[weightData['单品编码'] == int(row['单品编码'])]['贡献率'].values[0]
                priceSum += weight * row['销售单价(元/千克)']
            costSum = 0
            for index, row in itemCostData.iterrows():
                weight = weightData[weightData['单品编码'] == int(row['单品编码'])]['贡献率'].values[0]
                costSum += weight * row['批发价格(元/千克)']

            res_df.loc[len(res_df)] = [time, categoryCode,
                                       ((priceSum / priceWeightSum) if priceWeightSum != 0 else 0),
                                       ((costSum / costWeightSum) if costWeightSum != 0 else 0)]
    res_df.to_csv('../data/品类加权售价与成本.csv')


if __name__ == '__main__':
    price_cost_calculation()

import pandas as pd

file1 = '../附件1-蔬菜品类的商品信息.csv'
file2 = '../附件2-销售流水明细数据.csv'


def refactor_data():
    data = pd.read_csv(file2)
    total_sales = {}
    day_sales = {}
    cur_date = data['销售日期'][0]
    for index, row in data.iterrows():
        if row['销售日期'] != cur_date:
            total_sales[cur_date] = day_sales
            cur_date = row['销售日期']
            day_sales = {}
        if row['单品编码'] not in day_sales.keys():
            day_sales[row['单品编码']] = 0
        day_sales[row['单品编码']] += row['销量(千克)']
    columns = pd.read_csv(file1)['单品编码'].values
    rows = list(total_sales.keys())
    df = pd.DataFrame(index=rows, columns=columns)
    for day in rows:
        for item_code in columns:
            if item_code in total_sales[day].keys():
                df.at[day, item_code] = total_sales[day][item_code]
            else:
                df.at[day, item_code] = 0
    df.to_csv('../data/各单品对应日期的销售量.csv', float_format='%.f')


if __name__ == '__main__':
    print('重构单品对应日期销售量数据开始: ')
    refactor_data()
    print('重构单品对应日期销售量数据结束！ ')

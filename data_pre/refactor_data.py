import pandas as pd

file1 = '../附件1-蔬菜品类的商品信息.csv'
file2 = '../附件2-销售流水明细数据.csv'
file3 = '../data/各单品对应日期的销售量.csv'


def get_item_msg_by_code(code):
    data = pd.read_csv(file1)
    for index, row in data.iterrows():
        if row['单品编码'] == code:
            return {
                '单品编码': row['单品编码'],
                '单品名称': row['单品名称'],
                '分类编码': row['分类编码'],
                '分类名称': row['分类名称']
            }


def refactor_item_data():
    """
    重构蔬菜单品对应日期销售量数据
    :return: 各单品对应日期的销售量.csv
    """
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
    df.to_csv('../data/各单品对应日期的销售量.csv')


def refactor_cate_data():
    """
    重构蔬菜品类对应日期的销售量数据
    :return: 各蔬菜品类对应日期的销售量.csv
    """
    data = pd.read_csv(file3)
    total_sales = {}
    item_codes = pd.read_csv(file1)['单品编码'].values
    cate_code = set(pd.read_csv(file1)['分类编码'])
    rows = []
    for index, row in data.iterrows():
        day_sales = {}
        for code in cate_code:
            day_sales[code] = 0
        for code in item_codes:
            cate = get_item_msg_by_code(code)['分类编码']
            day_sales[cate] += row.loc[str(code)]
        total_sales[row.loc['date']] = day_sales
        rows.append(row.loc['date'])

    columns = list(cate_code)
    df = pd.DataFrame(index=rows, columns=columns)
    for day in rows:
        for cate in columns:
            df.at[day, cate] = total_sales[day][cate]
    df.to_csv('../data/各蔬菜品类对应日期的销售量.csv')


if __name__ == '__main__':
    # refactor_item_data()
    refactor_cate_data()

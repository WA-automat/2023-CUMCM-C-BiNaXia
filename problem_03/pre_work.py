import pandas as pd


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


def get_sale_items():
    """
    获取可售单品
    :return: 可售单品csv
    """
    days = ['2023-06-24', '2023-06-25', '2023-06-26', '2023-06-27', '2023-06-28', '2023-06-29', '2023-06-30']
    df = pd.read_csv('../附件2-销售流水明细数据.csv').iloc[-5000:]
    item_code_list = []
    for day in days:
        for idx, row in df.iterrows():
            if row['销售日期'] == day:
                item_code_list.append(row['单品编码'])
    item_code = set(item_code_list)
    item = {}
    for code in item_code:
        item[code] = get_item_msg_by_code(code)
    dfx = pd.DataFrame(columns=['单品编号', '单品名称', '分类编码', '分类名称'])
    for code in item_code:
        dfx.loc[len(dfx)] = [code, item[code]['单品名称'], item[code]['分类编码'], item[code]['分类名称']]
    print(dfx)
    dfx.to_csv('../data/2023年6月24-30可售单品信息.csv')


if __name__ == '__main__':
    get_sale_items()

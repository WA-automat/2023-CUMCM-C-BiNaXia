import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file1 = '../data/各单品对应日期的销售量.csv'
file2 = '../data/各蔬菜品类对应日期的销售量.csv'
file3 = '../附件1-蔬菜品类的商品信息.csv'

plt.style.use('seaborn')
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False


def get_item_msg_by_code(code):
    data = pd.read_csv(file3)
    for index, row in data.iterrows():
        if str(row['单品编码']) == code:
            return {
                '单品编码': row['单品编码'],
                '单品名称': row['单品名称'],
                '分类编码': row['分类编码'],
                '分类名称': row['分类名称']
            }


def get_cate_name_by_code(code):
    data = pd.read_csv(file3)
    for index, row in data.iterrows():
        if str(row['分类编码']) == str(code):
            return row['分类名称']


def cate_spearman():
    df = pd.read_csv(file2).iloc[:, 1:]
    corr_matrix = df.corr(method='spearman')
    print(corr_matrix)
    plt.figure(figsize=(10, 8))
    cols = corr_matrix.columns
    sticks = []
    for col in cols:
        sticks.append(get_cate_name_by_code(col))
    corr_matrix.to_csv('../data/六大蔬菜品类相关性.csv', index=True, header=True)
    sns.heatmap(corr_matrix, annot=True, cmap='PuBu', xticklabels=sticks, yticklabels=sticks, fmt='.3f')
    plt.savefig('../data/六大蔬菜品类相关性.png', dpi=300)
    plt.show()


def item_spearman():
    df = pd.read_csv(file1).iloc[:, 1:]
    corr_matrix = df.corr(method='spearman')
    corr_matrix.to_csv('../data/各蔬菜单品的相关性.csv')


def get_empty_sales_item():
    code = ['102900005116776', '102900005116042', '102900011023648', '102900011032145', '102900011011782']
    for i in code:
        print(get_item_msg_by_code(i))


if __name__ == '__main__':
    get_empty_sales_item()

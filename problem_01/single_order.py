import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller


def get_cate_name_by_code(code):
    data = pd.read_csv('../附件1-蔬菜品类的商品信息.csv')
    for index, row in data.iterrows():
        if str(row['分类编码']) == str(code):
            return row['分类名称']


def get_order_of_data(data):
    order = 0
    result = adfuller(data)
    while result[1] > 0.05:
        # 对序列进行一阶差分
        data = data.diff().dropna()
        # 再次进行ADF检验
        result = adfuller(data)
        # 差分阶数加1
        order += 1
    return order


def get_order_of_cate():
    file = '../data/各蔬菜品类对应日期的销售量.csv'
    df = pd.read_csv(file).iloc[:, 1:]
    for cate in df.columns:
        print(get_cate_name_by_code(cate) + '的n阶单整的阶数是' + str(get_order_of_data(df[cate])))


def draw_order_img():
    df = pd.read_csv('../data/各蔬菜品类对应日期的销售量.csv').iloc[:, 1:]
    cols = df.columns
    for col in cols:
        data = df[col]
        fig = plt.figure(figsize=(11, 3))
        """ ACF """
        ax1 = fig.add_subplot(121)
        fig = sm.graphics.tsa.plot_acf(data, lags=20, ax=ax1)
        fig.tight_layout()
        """ PACF """
        ax2 = fig.add_subplot(122)
        fig = sm.graphics.tsa.plot_pacf(data, lags=20, ax=ax2)
        fig.tight_layout()
        plt.savefig('../data/' + get_cate_name_by_code(col) + 'ACF+PACF.png', dpi=300)
        plt.show()


if __name__ == '__main__':
    draw_order_img()

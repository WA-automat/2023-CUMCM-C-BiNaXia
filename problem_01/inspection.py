import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

file1 = '../data/各单品对应日期的销售量.csv'
file2 = '../data/各蔬菜品类对应日期的销售量.csv'
file3 = '../附件1-蔬菜品类的商品信息.csv'


def get_cate_name_by_code(code):
    data = pd.read_csv(file3)
    for index, row in data.iterrows():
        if str(row['分类编码']) == code:
            return row['分类名称']


def draw_cate_norm_inspection(data):
    """
    :param data: 绘制分布直方图的数据
    :return: png
    """
    plt.style.use('ggplot')
    plt.rcParams['font.sans-serif'] = 'SimHei'
    plt.rcParams['axes.unicode_minus'] = False
    plt.subplots_adjust(wspace=0.45, hspace=0.3)

    col = data.columns

    for i in range(7):
        if i == 0:
            continue
        plt.subplot(2, 3, i)
        plt.hist(data[col[i]], bins='auto', color='steelblue', density=True)

        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        density = stats.gaussian_kde(data[col[i]])
        y = density(x)
        plt.plot(x, y, color='#CD5C5C')

        plt.xticks([])
        plt.title(get_cate_name_by_code(col[i]), fontsize=12)
        plt.ylabel('销售量', fontsize=10)
        plt.xlabel('时间', fontsize=10)
    plt.tight_layout()
    plt.savefig('../data/六大蔬菜品类销售量的分布直方图.png')
    plt.show()


def ks_inspection(data):
    """
    K-S检验数据正态性, p值大于0.05符合正态分布
    :param data: 要检验的数据
    :return: 元组(statistic,p_value)
    """
    data_mean = data.mean()
    data_std = data.std()
    return stats.kstest(data, 'norm', (data_mean, data_std))


if __name__ == '__main__':
    # data = pd.read_csv(file2)
    # draw_cate_norm_inspection(data)
    print()

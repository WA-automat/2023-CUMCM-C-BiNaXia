import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

file1 = '../data/各单品对应日期的销售量.csv'
file2 = '../data/各蔬菜品类对应日期的销售量.csv'
file3 = '../附件1-蔬菜品类的商品信息.csv'

plt.style.use('seaborn')
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
plt.subplots_adjust(wspace=0.45, hspace=0.3)


def get_cate_name_by_code(code):
    data = pd.read_csv(file3)
    for index, row in data.iterrows():
        if str(row['分类编码']) == code:
            return row['分类名称']


def draw_cate_dot_img():
    data = pd.read_csv(file2)
    cates = list(set(pd.read_csv(file3)['分类编码']))
    for idx, cate in enumerate(cates):
        plt.subplot(2, 3, idx + 1)
        y = data[str(cate)].values
        x = np.arange(len(y))
        plt.xlabel('时间', fontsize=9)
        plt.ylabel('销售量', fontsize=9)
        plt.xticks([])
        plt.title(get_cate_name_by_code(str(cate)), fontsize=10)
        plt.scatter(x, y, c='steelblue', s=10, alpha=0.5)
    plt.tight_layout()
    plt.savefig('../data/六大蔬菜品类销售量的散点图.png', dpi=300)
    plt.show()


if __name__ == '__main__':
    data = pd.read_csv(file1)
    item_code = ['102900005115885', '102900005118817', '102900005119975', '102900011032848', '102900011001561',
                 '102900011007969', '102900011000328', '102900011031582', '102900051004294']
    for idx, item in enumerate(item_code):
        plt.subplot(3, 3, idx + 1)
        y = data[item].values
        x = np.arange(len(y))
        plt.xlabel('时间', fontsize=9)
        plt.ylabel('销售量', fontsize=9)
        plt.xticks([])
        plt.scatter(x, y, c='steelblue', s=10, alpha=0.5)
    plt.tight_layout()
    plt.savefig('../data/部分蔬菜单品销售量的散点图.png', dpi=300)
    plt.show()

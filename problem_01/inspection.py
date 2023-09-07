import matplotlib.pyplot as plt
from scipy import stats


def draw_part_norm_inspection(data):
    print()


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
    print('绘制部分数据的正太分布曲线以及利用ks检验所有数据正态性')

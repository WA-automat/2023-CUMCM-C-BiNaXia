import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

file1 = '../data/各单品对应日期的销售量.csv'
file2 = '../data/各蔬菜品类对应日期的销售量.csv'

if __name__ == '__main__':
    x = np.arange(1084)
    y = pd.read_csv(file1)['102900011033531']
    plt.plot(x, y)
    plt.show()

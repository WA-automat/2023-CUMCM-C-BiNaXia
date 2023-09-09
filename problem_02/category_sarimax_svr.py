import math
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.svm import SVR
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import random

plt.style.use('seaborn')
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

file = '../data/品类加权售价与成本.csv'
sale = '../data/各蔬菜品类对应日期的销售量.csv'
file1 = '../附件1-蔬菜品类的商品信息.csv'
file2 = '../附件2-销售流水明细数据.csv'
file3 = '../附件3-蔬菜类商品批发价格.csv'
file4 = '../附件4-蔬菜类商品的近期损耗率.csv'

category = ['花叶类', '花菜类', '水生根茎类', '茄类', '辣椒类', '食用菌']
categoryCodes = [1011010101, 1011010201, 1011010402, 1011010501, 1011010504, 1011010801]
p = [2, 1, 1, 1, 1, 1]
d = [1, 0, 0, 0, 0, 0]
q = [0, 0, 0, 0, 0, 0]
s = 12
price_sarimax_models = []
price_svr_models = []
cost_sarimax_models = []
cost_svr_models = []
date = 1085
loss = [10.301386935220155, 13.345221045088197, 11.807853622477992,
        7.047093835603831, 8.510777941098349, 8.146985783749965]
c = np.array([])


def sarimax_svr(idx):
    weightMoneyData = pd.read_csv(file)
    saleData = pd.read_csv(sale)
    endog = saleData[str(categoryCodes[idx])].values

    # SARIMAX模型
    sarimax_model = SARIMAX(endog=endog,
                            exog=weightMoneyData[weightMoneyData['分类编码'] == categoryCodes[idx]]['加权售价'].values,
                            order=(p[idx], d[idx], q[idx]),
                            seasonal_order=(p[idx], d[idx], q[idx], s))
    model = sarimax_model.fit()
    pred_train = model.get_prediction()
    price_sarimax_models.append(model)

    y_true = saleData[str(categoryCodes[idx])].values
    y_pred = pred_train.predicted_mean

    print("预测销售量g函数：")

    print("----------------SARIMAX------------------")
    print("MSE:", mean_squared_error(y_true, y_pred))
    print("MAE:", mean_absolute_error(y_true, y_pred))
    print("R^2:", r2_score(y_true, y_pred))
    print("-----------------------------------------")

    # 结合SVR
    svr = SVR(C=150, gamma=0.3, epsilon=.1)
    svr.fit(X=np.arange(0, len(endog)).reshape(-1, 1), y=endog - pred_train.predicted_mean)
    price_svr_models.append(svr)

    # print(endog - pred_train.predicted_mean)
    # print(svr.predict(np.arange(0, len(endog)).reshape(-1, 1)))
    # plt.plot(endog - pred_train.predicted_mean)
    # plt.plot(svr.predict(np.arange(0, len(endog)).reshape(-1, 1)))

    y_true = saleData[str(categoryCodes[idx])].values
    y_pred = pred_train.predicted_mean + svr.predict(np.arange(0, len(endog)).reshape(-1, 1))

    # 绘图
    plt.title(category[idx] + '销售量预测')
    plt.plot(y_true, label='实际值')
    plt.plot(y_pred, label='预测值')
    plt.legend()
    plt.savefig('../data/' + str(idx) + '销售量预测.png', dpi=300)
    plt.show()

    print("--------------SARIMAX-SVR----------------")
    print("MSE:", mean_squared_error(y_true, y_pred))
    print("MAE:", mean_absolute_error(y_true, y_pred))
    print("R^2:", r2_score(y_true, y_pred))
    print("-----------------------------------------")

    endog = weightMoneyData[weightMoneyData['分类编码'] == categoryCodes[idx]]['加权成本'].values

    sarimax_model = SARIMAX(endog=endog,
                            order=(p[idx], d[idx], q[idx]),
                            seasonal_order=(p[idx], d[idx], q[idx], s))
    model = sarimax_model.fit()
    pred_train = model.get_prediction()
    cost_sarimax_models.append(model)

    y_true = weightMoneyData[weightMoneyData['分类编码'] == categoryCodes[idx]]['加权成本'].values
    y_pred = pred_train.predicted_mean

    print("预测成本h函数：")

    print("----------------SARIMAX------------------")
    print("MSE:", mean_squared_error(y_true, y_pred))
    print("MAE:", mean_absolute_error(y_true, y_pred))
    print("R^2:", r2_score(y_true, y_pred))
    print("-----------------------------------------")

    # 绘图
    # plt.plot(y_true)
    # plt.plot(y_pred)
    # plt.show()

    # 结合SVR
    svr = SVR(C=7, gamma=0.3, epsilon=.1)
    svr.fit(X=np.arange(0, len(endog)).reshape(-1, 1), y=endog - pred_train.predicted_mean)
    cost_svr_models.append(svr)

    y_true = weightMoneyData[weightMoneyData['分类编码'] == categoryCodes[idx]]['加权成本'].values
    y_pred = pred_train.predicted_mean + svr.predict(np.arange(0, len(endog)).reshape(-1, 1))

    print("--------------SARIMAX-SVR----------------")
    print("MSE:", mean_squared_error(y_true, y_pred))
    print("MAE:", mean_absolute_error(y_true, y_pred))
    print("R^2:", r2_score(y_true, y_pred))
    print("-----------------------------------------")

    # 绘图
    # plt.plot(y_true)
    # plt.plot(y_pred)
    # plt.show()


def solve(idx, length, c1, c2):
    # 导入模型
    price_sarimax = price_sarimax_models[idx]
    price_svr = price_svr_models[idx]
    cost_sarimax = cost_sarimax_models[idx]
    cost_svr = cost_svr_models[idx]

    # 利用模型预测销售量
    cp = np.append(c, np.array([c1]))
    n1 = price_sarimax.get_forecast(steps=length, exog=cp.reshape(-1, 1)).predicted_mean[-1] + \
         price_svr.predict(np.array([date + length - 1]).reshape(-1, 1))[0]
    cp = np.append(c, np.array([c2]))
    n2 = price_sarimax.get_forecast(steps=length, exog=cp.reshape(-1, 1)).predicted_mean[-1] + \
         price_svr.predict(np.array([date + length - 1]).reshape(-1, 1))[0]
    n = n1 + n2

    # 售出量
    P = n1 * c1 + n2 * c2
    # 利用模型预测成本d
    D = cost_sarimax.get_forecast(steps=length).predicted_mean[-1] + \
        cost_svr.predict(np.array([date + length - 1]).reshape(-1, 1))[0]

    return P - n * D, n


def SA(idx, length):
    C = [9, 7]
    cur_price = solve(idx, length, C[0], C[1])[0]

    best_c = C.copy()
    best_price = cur_price

    # 控制参数
    initial_temperature = 100.0
    final_temperature = 1
    cooling_rate = 0.93
    iterations_per_temperature = 50

    # 模拟退火主循环
    temperature = initial_temperature
    while temperature > final_temperature:
        for _ in range(iterations_per_temperature):
            # 生成邻域解
            neighbor_solution = [C[0] + random.uniform(-1, 1),
                                 C[1] + random.uniform(-1, 1)]
            neighbor_price, tmpN = solve(idx, length, neighbor_solution[0], neighbor_solution[1])

            # 不满足条件
            if neighbor_solution[0] < 0 or neighbor_solution[1] < 0 or \
                    neighbor_solution[0] < neighbor_solution[1] or tmpN < 0 or \
                    neighbor_solution[0] > 30 or neighbor_solution[1] > 20 or \
                    neighbor_price < 0:
                continue

            # 接受邻域解或者以一定概率接受不良解
            if neighbor_price > cur_price or random.uniform(0, 1) < math.exp(
                    (neighbor_price - cur_price) / temperature):
                C = neighbor_solution
                cur_price = neighbor_price

                # 更新最优解
                if cur_price > best_price:
                    best_c = C.copy()
                    best_price = cur_price

        temperature *= cooling_rate  # 降低温度

    return best_price, best_c, solve(idx, length, best_c[0], best_c[1])[1]


if __name__ == '__main__':
    for i in range(6):
        sarimax_svr(i)
    for i in range(6):
        c = np.array([])
        for j in range(7):
            sa = SA(i, j + 1)
            c = np.append(c, (1 - loss[i]) * sa[1][0] + loss[i] * sa[1][1])
            print("i = ", i, " j = ", j)
            print(sa)
        print(c)

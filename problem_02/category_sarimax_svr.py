import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.svm import SVR
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

file = '../data/品类加权售价与成本.csv'
sale = '../data/各蔬菜品类对应日期的销售量.csv'
file1 = '../附件1-蔬菜品类的商品信息.csv'
file2 = '../附件2-销售流水明细数据.csv'
file3 = '../附件3-蔬菜类商品批发价格.csv'
file4 = '../附件4-蔬菜类商品的近期损耗率.csv'

categoryCodes = [1011010101, 1011010201, 1011010402, 1011010501, 1011010504, 1011010801]
p = [2, 1, 1, 1, 1, 1]
d = [1, 0, 0, 0, 0, 0]
q = [0, 0, 0, 0, 0, 0]
s = 12
price_sarimax_models = []
price_svr_models = []
cost_sarimax_models = []
cost_svr_models = []


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
    # plt.plot(y_true)
    # plt.plot(y_pred)
    # plt.show()

    print("--------------SARIMAX-SVR----------------")
    print("MSE:", mean_squared_error(y_true, y_pred))
    print("MAE:", mean_absolute_error(y_true, y_pred))
    print("R^2:", r2_score(y_true, y_pred))
    print("-----------------------------------------")

    sarimax_model = SARIMAX(endog=weightMoneyData[weightMoneyData['分类编码'] == categoryCodes[idx]]['加权成本'].values,
                            order=(p[idx], d[idx], q[idx]),
                            seasonal_order=(p[idx], d[idx], q[idx], s))
    model = sarimax_model.fit()
    pred_train = model.get_prediction()
    cost_sarimax_models.append(model)

    y_true = saleData[str(categoryCodes[idx])].values
    y_pred = pred_train.predicted_mean

    print("预测成本h函数：")

    print("----------------SARIMAX------------------")
    print("MSE:", mean_squared_error(y_true, y_pred))
    print("MAE:", mean_absolute_error(y_true, y_pred))
    print("R^2:", r2_score(y_true, y_pred))
    print("-----------------------------------------")

    # 绘图
    plt.plot(y_true)
    plt.plot(y_pred)
    plt.show()

    # 结合SVR
    svr = SVR(C=150, gamma=0.3, epsilon=.1)
    svr.fit(X=np.arange(0, len(endog)).reshape(-1, 1), y=endog - pred_train.predicted_mean)
    cost_svr_models.append(svr)

    y_true = saleData[str(categoryCodes[idx])].values
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


if __name__ == '__main__':
    for i in range(6):
        sarimax_svr(i)

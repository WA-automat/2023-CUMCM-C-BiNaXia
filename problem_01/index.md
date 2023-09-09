### 问题一：

1. 总销售量为0单品：

   {'单品编码': 102900005116776, '单品名称': '本地菠菜', '分类编码': 1011010101, '分类名称': '花叶类'}
   {'单品编码': 102900005116042, '单品名称': '藕', '分类编码': 1011010402, '分类名称': '水生根茎类'}
   {'单品编码': 102900011023648, '单品名称': '芜湖青椒(2)', '分类编码': 1011010504, '分类名称': '辣椒类'}
   {'单品编码': 102900011032145, '单品名称': '芜湖青椒(份)', '分类编码': 1011010504, '分类名称': '辣椒类'}
   {'单品编码': 102900011011782, '单品名称': '虫草花(盒)(1)', '分类编码': 1011010801, '分类名称': '食用菌'}

2. 品类的n阶单整：

   水生根茎类的n阶单整的阶数是0
   茄类的n阶单整的阶数是0
   辣椒类的n阶单整的阶数是0
   食用菌的n阶单整的阶数是0
   花叶类的n阶单整的阶数是1
   花菜类的n阶单整的阶数是0

   >除了花叶类都是同阶单整

3. 同阶单整的各蔬菜品类两两之间存在协整关系（利用的是Johansen 协整性测试）

4. 同阶单整品类的格兰杰因果检验：

   Granger 因果性检验给出了四种统计检验的结果：SSR 基础的 F 测试、SSR 基础的卡方测试（Chi2）、似然比测试（Likelihood Ratio）和参数 F 测试。每个测试都有其对应的 p 值。一般来说，我们可以选择 SSR 基础的 F 测试的 p 值，这是因为 F 测试是常用的并且在 Granger 因果性检验中最常被报告的。（下面是一个结果例子）

   ```tex
   Granger Causality
   number of lags (no zero) 1
   ssr based F test:         F=4.6483  , p=0.0313  , df_denom=1080, df_num=1
   ssr based chi2 test:   chi2=4.6612  , p=0.0309  , df=1
   likelihood ratio test: chi2=4.6512  , p=0.0310  , df=1
   parameter F test:         F=4.6483  , p=0.0313  , df_denom=1080, df_num=1
   ```

   一般用ssr based F test的p值进行判断，如果p<0.05则说明某个序列对另一个序列有预测能力或两者有因果关系

   （对于下面的两两，如果p值小于0.05则表示后者对于前者有预测能力）

   * 花菜类与水生根茎类:

     ```tex
     Granger Causality
     number of lags (no zero) 1
     ssr based F test:         F=0.5859  , p=0.4442  , df_denom=1080, df_num=1
     ssr based chi2 test:   chi2=0.5875  , p=0.4434  , df=1
     likelihood ratio test: chi2=0.5874  , p=0.4434  , df=1
     parameter F test:         F=0.5859  , p=0.4442  , df_denom=1080, df_num=1
     ```

   * 花菜类与茄类:

     ```tex
     Granger Causality
     number of lags (no zero) 1
     ssr based F test:         F=4.6483  , p=0.0313  , df_denom=1080, df_num=1
     ssr based chi2 test:   chi2=4.6612  , p=0.0309  , df=1
     likelihood ratio test: chi2=4.6512  , p=0.0310  , df=1
     parameter F test:         F=4.6483  , p=0.0313  , df_denom=1080, df_num=1
     ```

   * 花菜类与辣椒类:

     ```tex
     Granger Causality
     number of lags (no zero) 1
     ssr based F test:         F=0.3619  , p=0.5476  , df_denom=1080, df_num=1
     ssr based chi2 test:   chi2=0.3629  , p=0.5469  , df=1
     likelihood ratio test: chi2=0.3629  , p=0.5469  , df=1
     parameter F test:         F=0.3619  , p=0.5476  , df_denom=1080, df_num=1
     ```

   * 花菜类与食用菌:

     ```tex
     Granger Causality
     number of lags (no zero) 1
     ssr based F test:         F=0.5698  , p=0.4505  , df_denom=1080, df_num=1
     ssr based chi2 test:   chi2=0.5714  , p=0.4497  , df=1
     likelihood ratio test: chi2=0.5712  , p=0.4498  , df=1
     parameter F test:         F=0.5698  , p=0.4505  , df_denom=1080, df_num=1
     ```

   * 水生根茎类与花菜类:

     ```tex
     Granger Causality
     number of lags (no zero) 1
     ssr based F test:         F=0.0741  , p=0.7855  , df_denom=1080, df_num=1
     ssr based chi2 test:   chi2=0.0743  , p=0.7851  , df=1
     likelihood ratio test: chi2=0.0743  , p=0.7851  , df=1
     parameter F test:         F=0.0741  , p=0.7855  , df_denom=1080, df_num=1
     ```

   * 水生根茎类与茄类:

     ```tex
     Granger Causality
     number of lags (no zero) 1
     ssr based F test:         F=38.9561 , p=0.0000  , df_denom=1080, df_num=1
     ssr based chi2 test:   chi2=39.0643 , p=0.0000  , df=1
     likelihood ratio test: chi2=38.3763 , p=0.0000  , df=1
     parameter F test:         F=38.9561 , p=0.0000  , df_denom=1080, df_num=1
     ```

   * 水生根茎类与辣椒类:

     ```tex
     Granger Causality
     number of lags (no zero) 1
     ssr based F test:         F=0.1486  , p=0.7000  , df_denom=1080, df_num=1
     ssr based chi2 test:   chi2=0.1490  , p=0.6995  , df=1
     likelihood ratio test: chi2=0.1490  , p=0.6995  , df=1
     parameter F test:         F=0.1486  , p=0.7000  , df_denom=1080, df_num=1
     ```

   * 水生根茎类与食用菌:

     ```tex
     Granger Causality
     number of lags (no zero) 1
     ssr based F test:         F=2.5229  , p=0.1125  , df_denom=1080, df_num=1
     ssr based chi2 test:   chi2=2.5299  , p=0.1117  , df=1
     likelihood ratio test: chi2=2.5270  , p=0.1119  , df=1
     parameter F test:         F=2.5229  , p=0.1125  , df_denom=1080, df_num=1
     ```

   * 茄类与花菜类:

     ```tex
     Granger Causality
     number of lags (no zero) 1
     ssr based F test:         F=5.3017  , p=0.0215  , df_denom=1080, df_num=1
     ssr based chi2 test:   chi2=5.3164  , p=0.0211  , df=1
     likelihood ratio test: chi2=5.3034  , p=0.0213  , df=1
     parameter F test:         F=5.3017  , p=0.0215  , df_denom=1080, df_num=1
     ```

   * 茄类与水生根茎类:

     ```tex
     Granger Causality
     number of lags (no zero) 1
     ssr based F test:         F=33.9265 , p=0.0000  , df_denom=1080, df_num=1
     ssr based chi2 test:   chi2=34.0207 , p=0.0000  , df=1
     likelihood ratio test: chi2=33.4973 , p=0.0000  , df=1
     parameter F test:         F=33.9265 , p=0.0000  , df_denom=1080, df_num=1
     ```

   * 茄类与辣椒类:

     ```tex
     Granger Causality
     number of lags (no zero) 1
     ssr based F test:         F=21.2354 , p=0.0000  , df_denom=1080, df_num=1
     ssr based chi2 test:   chi2=21.2943 , p=0.0000  , df=1
     likelihood ratio test: chi2=21.0877 , p=0.0000  , df=1
     parameter F test:         F=21.2354 , p=0.0000  , df_denom=1080, df_num=1
     ```

   * 茄类与食用菌:

     ```tex
     Granger Causality
     number of lags (no zero) 1
     ssr based F test:         F=26.8144 , p=0.0000  , df_denom=1080, df_num=1
     ssr based chi2 test:   chi2=26.8888 , p=0.0000  , df=1
     likelihood ratio test: chi2=26.5605 , p=0.0000  , df=1
     parameter F test:         F=26.8144 , p=0.0000  , df_denom=1080, df_num=1
     ```

   * 辣椒类与花菜类:

     ```tex
     Granger Causality
     number of lags (no zero) 1
     ssr based F test:         F=0.0078  , p=0.9296  , df_denom=1080, df_num=1
     ssr based chi2 test:   chi2=0.0078  , p=0.9295  , df=1
     likelihood ratio test: chi2=0.0078  , p=0.9295  , df=1
     parameter F test:         F=0.0078  , p=0.9296  , df_denom=1080, df_num=1
     ```

   * 辣椒类与水生根茎类:

     ```tex
     Granger Causality
     number of lags (no zero) 1
     ssr based F test:         F=1.2868  , p=0.2569  , df_denom=1080, df_num=1
     ssr based chi2 test:   chi2=1.2904  , p=0.2560  , df=1
     likelihood ratio test: chi2=1.2896  , p=0.2561  , df=1
     parameter F test:         F=1.2868  , p=0.2569  , df_denom=1080, df_num=1
     ```

   * 辣椒类与茄类:

     ```tex
     Granger Causality
     number of lags (no zero) 1
     ssr based F test:         F=21.0333 , p=0.0000  , df_denom=1080, df_num=1
     ssr based chi2 test:   chi2=21.0918 , p=0.0000  , df=1
     likelihood ratio test: chi2=20.8890 , p=0.0000  , df=1
     parameter F test:         F=21.0333 , p=0.0000  , df_denom=1080, df_num=1
     ```

   * 辣椒类与食用菌:

     ```tex
     Granger Causality
     number of lags (no zero) 1
     ssr based F test:         F=0.0936  , p=0.7597  , df_denom=1080, df_num=1
     ssr based chi2 test:   chi2=0.0939  , p=0.7593  , df=1
     likelihood ratio test: chi2=0.0939  , p=0.7593  , df=1
     parameter F test:         F=0.0936  , p=0.7597  , df_denom=1080, df_num=1
     ```

   * 食用菌与花菜类:

     ```tex
     Granger Causality
     number of lags (no zero) 1
     ssr based F test:         F=0.3822  , p=0.5366  , df_denom=1080, df_num=1
     ssr based chi2 test:   chi2=0.3832  , p=0.5359  , df=1
     likelihood ratio test: chi2=0.3832  , p=0.5359  , df=1
     parameter F test:         F=0.3822  , p=0.5366  , df_denom=1080, df_num=1
     ```

   * 食用菌与水生根茎类:

     ```tex
     Granger Causality
     number of lags (no zero) 1
     ssr based F test:         F=0.0084  , p=0.9270  , df_denom=1080, df_num=1
     ssr based chi2 test:   chi2=0.0084  , p=0.9269  , df=1
     likelihood ratio test: chi2=0.0084  , p=0.9269  , df=1
     parameter F test:         F=0.0084  , p=0.9270  , df_denom=1080, df_num=1
     ```

   * 食用菌与茄类:

     ```tex
     Granger Causality
     number of lags (no zero) 1
     ssr based F test:         F=33.0898 , p=0.0000  , df_denom=1080, df_num=1
     ssr based chi2 test:   chi2=33.1817 , p=0.0000  , df=1
     likelihood ratio test: chi2=32.6835 , p=0.0000  , df=1
     parameter F test:         F=33.0898 , p=0.0000  , df_denom=1080, df_num=1
     ```

   * 食用菌与辣椒类:

     ```tex
     Granger Causality
     number of lags (no zero) 1
     ssr based F test:         F=0.5490  , p=0.4589  , df_denom=1080, df_num=1
     ssr based chi2 test:   chi2=0.5505  , p=0.4581  , df=1
     likelihood ratio test: chi2=0.5504  , p=0.4582  , df=1
     parameter F test:         F=0.5490  , p=0.4589  , df_denom=1080, df_num=1
     ```

   

4. 品类的ACT+PACF

   （具体见压缩包）
   
4. 品类的ks检验结果
* 水生根茎类: KstestResult(statistic=0.1253645216269794, pvalue=2.6172413606389837e-15, statistic_location=1.809, statistic_sign=-1)
* 茄类: KstestResult(statistic=0.09035868929543822, pvalue=3.757573883369016e-08, statistic_location=23.119, statistic_sign=1)
* 辣椒类: KstestResult(statistic=0.1366617781781262, pvalue=4.039664429926888e-18, statistic_location=89.474, statistic_sign=1)
* 食用菌: KstestResult(statistic=0.11654298730943269, pvalue=2.770231366567422e-13, statistic_location=75.963, statistic_sign=1)
* 花叶类: KstestResult(statistic=0.0748450891326713, pvalue=9.987520574262495e-06, statistic_location=227.336, statistic_sign=1)
* 花菜类: KstestResult(statistic=0.0909264419929724, pvalue=3.0025933529838453e-08, statistic_location=35.261, statistic_sign=1)

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
#matplotlib.style.use('ggplot')

if False:
    df = pd.DataFrame(np.random.randn(1000, 4), columns=list('ABCD'))

    df = df.cumsum()

    plt.figure()
    df.plot()
    plt.show()


if False:
    df2 = pd.DataFrame(np.random.randn(1000, 1), columns=['A'])
    df3 = pd.DataFrame(np.random.randn(1000, 1), columns=['B'])

    df_new = pd.concat([df2, df3])
    df_new = df_new.cumsum()
    plt.figure()
    df_new.plot()
    plt.show()



# demonstrate merging of data with differing index
if True:
    ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
    ts1 = pd.Series(np.random.randn(1000), index=pd.date_range('6/1/2000', periods=1000))
    #ts = ts.cumsum()

    df2 = pd.DataFrame(np.random.randn(1000, 1), index=ts.index, columns=['A'])
    df3 = pd.DataFrame(np.random.randn(1000, 1), index=ts1.index, columns=['B'])
    df_new = pd.concat([df2, df3])
    df_new = df_new.cumsum()
    plt.figure()
    df_new.plot()
    plt.show()


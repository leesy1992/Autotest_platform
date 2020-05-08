# import pandas as pd
# import numpy as np
#
# df = pd.DataFrame(np.random.randn(10,4),index=pd.date_range('2018/12/18',
#    periods=10), columns=list('ABCD'))
#
# df.plot()
# import matplotlib.pyplot as plt
#
# squares = [1, 4, 9, 16, 25]
# plt.plot(squares, linewidth=5)
#
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
#
# plt.tick_params(axis='both', labelsize=12)
# plt.show()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
#matplotlib inline
np.random.seed(100)
df = pd.DataFrame(np.random.randint(-10, 10, (10, 3)),
                  index=pd.date_range("1/1/2000", periods=10), columns=list("ABC"))
df = df.cumsum()
df.head()
df


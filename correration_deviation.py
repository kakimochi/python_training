
# coding: utf-8

# In[10]:

import numpy as np

x = [1, 2, 3, 4, 5]
y = [0, 2, 4, 5, 8]

# 標準偏差
print np.std(x)
print np.std(x, ddof=1)

# 相関係数
print np.corrcoef(x, y)[0, 1]


# In[ ]:




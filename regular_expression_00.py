
# coding: utf-8

# In[3]:

import re

text = '012--345--67890'
pattern = '\d+'

l = re.findall(pattern, text)

print(l)


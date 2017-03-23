
# coding: utf-8

# In[3]:

import re

pattern = '(blue|white|red)'
replace = 'color'
text = 'blue socks and red shoes'

p = re.compile(pattern)
result = p.sub(replace, text)

print (result)


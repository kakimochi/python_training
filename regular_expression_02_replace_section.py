
# coding: utf-8

# In[4]:

import re

pattern = 'section{ ( [^}]* ) }'
replace = r'hoge{\1}'
text = 'section{1st} section{2nd}'

p = re.compile(pattern, re.VERBOSE)
result = p.sub(replace, text)

print (text)
print (result)


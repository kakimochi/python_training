
# coding: utf-8

# In[8]:


# 例外処理
fruits = {
    'apple' : 100,
    'orange' : 50,
}

def calc_fruit_amount(name, count):
    try:
        return fruits[name] * count
    except:
        print('{} does not exist in the record.', format(name))


# In[7]:

calc_fruit_amount('apple', 5)


# In[9]:

calc_fruit_amount('hogehoge', 3)


# In[ ]:




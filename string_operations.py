
# coding: utf-8

# In[2]:

# 文字列連結
a = 'Hello'
b = ' '
c = 'World!'

print a + b + c


# In[5]:

# joinメソッドで連結
strings = ['dog', 'cat', 'penguin']
print 'でしょ！'.join(strings)


# In[7]:

# 繰り返し
s = 'penguinでしょ！'
print s * 3


# In[16]:

# spinrtf
a = 99.9999
print '%.4f' % a
print '%.2f' % a #四捨五入されるようだ


# In[18]:

# リストそのまま表示
a_list = (1, 2, 3)
print 'list is: %s' % (a_list,)


# In[19]:

# 正規表現で置換
import re
s = 'Hello World'
print re.sub(r"[a-z]", "A", s)


# In[22]:

# n文字目の文字を取得
s = '0123456789'
print s[0] #0番目
print s[5] #5番目
print s[-1] #最後


# In[25]:

# 部分文字列の取得
s = '0123456789'
print s[0:2] #0番目から-2番目までを抽出
print s[-4:-1] #最後から3文字を抽出


# In[31]:

# 文字列を検索
s = '0123456789'
print s.find('5')
print s.find('5', 6) # 2文字目から検索(みつからなければ-1が返る)


# In[35]:

# すべてを検索
s = '012345123451234512345'
find_str = '51'
index = -1
while True:
    index = s.find(find_str, index + 1)
    if index == -1:
        break
    print 'index = %d' % index


# In[46]:

# 1文字ずつ処理
for char in '0123':
    print char + 'です'

# リストで取り出す
print list('hoge')

# インデックスで参照
s = '0123'
for i in range(len(s)):
    print str(i) + '番目は' + str(s[i]) + 'です'


# In[47]:

# 両端のspace削除
s = '  012   '
print s.strip()


# In[48]:

# カウント
s = '0123\n0123\n0123\n'
print s.count('\n')


# In[ ]:




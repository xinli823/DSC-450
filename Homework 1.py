#!/usr/bin/env python
# coding: utf-8

# In[1]:


def generateInsert(name,values):
    return 'INSERT INTO ' + name + ' VALUES ' + '(' + ','.join(values) + ')'


# In[2]:


print(generateInsert('Students', ['1', 'Jane', 'A+']))


# In[3]:


generateInsert('Phone',['42','312-555-1212'])


# In[ ]:





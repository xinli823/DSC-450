#!/usr/bin/env python
# coding: utf-8

# In[118]:


def validateInsert(values):
    if values[:11] == 'INSERT INTO' and values[-1] == ';':
        value = values.replace(';','') # remove ;
        value = value.split('VALUES') # split original string ar VALUES
        table = value[0].split(' ')[2] # split again to get table name
        return 'Inserting' + value[1] + ' into ' + table +' table'
    else:
        return 'Invalid insert'


# In[119]:


validateInsert('INSERT INTO Students VALUES (1, Jane, A+);')


# In[120]:


validateInsert('INSERT INTO Students VALUES (1, Jane, A+)')


# In[122]:


validateInsert('INSERT Students VALUES (1, Jane, A+);')


# In[121]:


validateInsert('INSERT INTO Phones VALUES (42, 312-555-1212);')


# In[ ]:





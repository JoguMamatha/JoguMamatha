#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def upper1(strin):
    a=""
    for x in strin:
        if ord(x)>=97 and ord(x)<=122:
            a+=chr(ord(x)-32)
        else:
            a+=x
    return a


# In[ ]:


def lower1(strin):
    a=""
    for x in strin:
        if ord(x)>=65 and ord(x)<=90:
            a+=chr(ord(x)+32)
        else:
            a+=x
    return a   


# In[ ]:


def isupper1(strin):
    for x in strin:
        if ord(x)>=97 and ord(x)<=122:
            return False
        else:
            continue
    return True


# In[ ]:


def islower1(strin):
    for x in strin:
        if ord(x)>=65 and ord(x)<=90:
            return False
        else:
            continue
    return True


# In[3]:


def isdigit1(strin):
    for x in strin:
        if ord(x)>=48 and ord(x)<=57:
            continue
        else:
            return False
    return True


# In[ ]:


def title1(st):
    s="";a=0
    for x in st:
        if x==" ":
            a=0
            for y in x:
                if (ord(x)>=97 and ord(x)<=122) and a==0:
                    s+=chr(ord(x)-32)
                    a+=1
                elif ord(x)>=65 and ord(x)<=90 and not(a==0):
                    s+=chr(ord(x)+32)
                    a+=1
                else:
                    s+=x
        elif a==0:
            if (ord(x)>=97 and ord(x)<=122):
                s+=chr(ord(x)-32)
                a+=1
            elif ord(x)>=65 and ord(x)<=90:
                s+=x
            else:
                s+=x
        else:
            if ord(x)>=65 and ord(x)<=90:
                s+=chr(ord(x)+32)
            else:
                s+=x
    return s


# In[4]:


def cap1(st):
    s=""
    for x in range(len(st)):
        if x==0:
            if ord(st[0])<=122 and ord(st[0])>=97:
                s+=chr(ord(st[0])-32)
            else:
                s+=st[x]
        else:
            if st[x-1]==" ":
                if ord(st[x])<=122 and ord(st[x])>=97:
                    s+=chr(ord(st[x])-32)
                    continue
                else:
                    s+=st[x]
                    continue
            elif ord(st[x])>=65 and ord(st[x])<=90:
                s+=chr(ord(st[x])+32)
            else:
                s+=st[x]
    return s


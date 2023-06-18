#!/usr/bin/env python
# coding: utf-8

# In[1]:


#a
#Create a python program to print the below pattern using for loop as or while loop
#1  
#2 2  
#3 3 3  
#4 4 4 4  
#5 5 5 5 5

for x in range(1,6):
    for y in range(1,x+1):
        print(x,end=" ")
    print()


# In[2]:


#b
#1 
#1 2 
#1 2 3 
#1 2 3 4 
#1 2 3 4 5

for x in range(1,6):
    for y in range(1,x+1):
        print(y, end=" ")
    print()


# In[3]:


#c
#1 1 1 1 1 
#2 2 2 2 
#3 3 3 
#4 4 
#5

for x in range(1,6):
    for y in range(6,x,-1):
        print(x,end=" ")
    print()


# In[4]:


#d
#5 5 5 5 5 
#5 5 5 5 
#5 5 5 
#5 5 
#5

for x in range(5,0,-1):
    for y in range(0,x):
        print("5",end=" ")
    print()


# In[5]:


#e
#0 1 2 3 4 5 
#0 1 2 3 4 
#0 1 2 3 
#0 1 2 
#0 1

for x in range(5,0,-1):
    for y in range(0,x+1):
        print(y,end=" ")
    print()


# In[6]:


#f
#1 
#3 3 
#5 5 5 
#7 7 7 7 
#9 9 9 9 9

for x in range(1,10,2):
    for y in range(1,x+1,2):
        print(x,end=" ")
    print()


# In[7]:


#g
#5 5 5 5 5 
#4 4 4 4 
#3 3 3 
#2 2 
#1

for x in range(5,0,-1):
    for y in range(x,0,-1):
        print(x,end=" ")
    print()


# In[8]:


#h
#1 
#2 1 
#3 2 1 
#4 3 2 1 
#5 4 3 2 1

for x in range(1,6):
    for y in range(x,0,-1):
        print(y,end=" ")
    print()


# In[9]:


#i
#5 4 3 2 1 
#4 3 2 1 
#3 2 1 
#2 1 
#1

for x in range(0,5):
    for y in range(5,x,-1):
        print(y,end=" ")
    print()


# In[10]:


#j)
#1
#3 2
#6 5 4
#10 9 8 7
x=1
y=2
a=y
for i in range(2, 6):
    for j in range(x,y):
        a-=1
        print(a,end=' ')
    print()
    x=y
    y+=i
    a=y


# In[11]:


#k
#          1 
#        1 2 
#      1 2 3 
#    1 2 3 4 
#  1 2 3 4 5 

for x in range(7,1,-1):
    z=1
    for y in range(1,7):
        if x>y:
            print(" ",end=" ")
        else:
            print(z,end=" ")
            z+=1
    print()
    


# In[12]:


#m
#1 2 3 4 5 
#2 2 3 4 5 
#3 3 3 4 5 
#4 4 4 4 5 
#5 5 5 5 5

for x in range(1,6):
    for y in range(1,6):
        if y<=x:
            print(x,end=" ")
        else:
            print(y,end=" ")
    print()


# In[15]:


#n
#1  
#2  4  
#3  6  9  
#4  8  12  16  
#5  10  15  20  25  
#6  12  18  24  30  36  
#7  14  21  28  35  42  49  
#8  16  24  32  40  48  56  64

for x in range(1,9):
    z=1
    for y in range(1,x+1):
        print(x*z,end=" ")
        z+=1
    print(z)


# In[16]:


#o
#* 
#* * 
#* * * 
#* * * * 
#* * * * *

for x in range(0,5):
    for y in range(0,x+1):
        print("*",end=" ")
    print()


# In[17]:


#p
#     * 
#    ** 
#   *** 
#  **** 
# ***** 

for x in range(5,0,-1):
    print(" "*x,end="")
    for y in range(6,x,-1):
        print("*",end="")
    print()


# In[18]:


#q
#* * * * *  
#* * * *  
#* * *  
#* *  
#*

for x in range(6,0,-1):
    for y in range(0,x-1):
        print("*",end=" ")
    print()


# In[19]:


#r
#       * * * * * * 
#        * * * * * 
#         * * * * 
#          * * * 
#           * * 
#            * 

for x in range(0,6):
    print(" "*x,end="")
    for y in range(6,x,-1):
        print("*",end=" ")
    print()


# In[20]:


#s
#*****
# ****
#  ***
#   **
#    *

for x in range(0,5):
    print(" "*x,end="")
    for y in range(5,x,-1):
        print("*",end="")
    print()


# In[21]:


#t
#            *   
#           *  *   
#          *  *  *   
#         *  *  *  *   
#        *  *  *  *  *   
#       *  *  *  *  *  *   
#      *  *  *  *  *  *  *   

for x in range(7,0,-1):
    print(" "*x,end="")
    for y in range(8,x,-1):
        print("*",end=" ")
    print()


# In[22]:


#u
#*  
#* *  
#* * *  
#* * * *  
#* * * * *  
#* * * * * *  
# 
#* * * * * *  
#* * * * *  
#* * * *  
#* * *  
#* *  
#*

for x in range(1,14):
    if x<7:
        for y in range(1,x+1):
            print("*",end=" ")
    elif x==7:
        print(end="")
    else:
        for y in range(14-x,0,-1):
            print("*",end=" ")
    print()


# In[23]:


#v
#* 
#* * 
#* * * 
#* * * * 
#* * * * * 
#* * * * 
#* * * 
#* * 
#* 

for x in range(1,10):
    if x<6:
        for y in range(1,x+1):
            print("*",end=" ")
    else:
        for y in range(10-x,0,-1):
            print("*",end=" ")
    print()


# In[24]:


#w

#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 
#   * * * * 
#     * * * 
#       * * 
#         * 

for x in range(5,0,-1):
    print(" "*x,end="")
    for y in range(6,x,-1):
        print("*",end="")
    print()
for x in range (1,5):
    print(" "*x,end=" ")
    for y in range(4,x-1,-1):
        print("*",end="")
    print()


# In[25]:


#x
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 

for x in range(0,5):
    print(" "*x,end="")
    for y in range(5,x,-1):
        print("*",end=" ")
    print()
a=2
for x in range(4,-1,-1):
    print(" "*x,end="")
    for y in range(1,a):
        print("*",end=" ")
    a+=1
    print()


# In[26]:


#y
#        * 
#       * * 
#      * * * 
#     * * * * 
#    * * * * * 
#   * * * * * * 
#    * * * * * 
#     * * * * 
#      * * * 
#       * * 
#        * 

for x in range(6,0,-1):
    print(" "*x,end="")
    for y in range(7,x,-1):
        print("*",end=" ")
    print()
for x in range (1,6):
    print(" "*x,end=" ")
    for y in range(5,x-1,-1):
        print("*",end=" ")
    print()


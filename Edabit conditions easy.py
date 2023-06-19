#!/usr/bin/env python
# coding: utf-8

# In[4]:


#1 Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name, return the 
#relation of that person to Luke.
# Person 	Relation
# Darth Vader	father
# Leia	 sister
# Han	 brother in law
# R2D2	 droid

def relation_to_luke(name):
    relation={"darth vader":"father","leia":"sister","han":"brother in law","r2d2":"droid"}
    for z in relation:
        if name.lower()==z:
            return ("Luke, I am your {}.".format(relation[x]))
        else:
            continue


# In[2]:


relation_to_luke("Darth Vader")


# In[3]:


relation_to_luke("Leia")


# In[5]:


#2 Create a function that takes damage and speed (attacks per second) and returns the amount of damage after a 
#given time.

def damage(d,s,t):
    if d>=0 and s>=0:
        if t.lower()=="second":
            return d*s
        elif t.lower()=="minute":
            return d*s*60
        else:
            return d*s*3600
    else:
        return "invalid input"


# In[7]:


damage(30, 5, "second")


# In[8]:


#3 Create a function that takes a number as input and returns True if the sum of its digits has the same parity as
#the entire number. Otherwise, return False.

def parity_analysis(n):
    m=n;s=0
    if n/10<0:
        return True
    else:
        while n>=1:
            a=n%10
            s+=a
            n//=10
        return (m%2==s%2)


# In[10]:


parity_analysis(133)


# In[11]:


#4 Create a function that takes a string, checks if it has the same number of "x"s and "o"s and returns either 
#True or False.
#Return a boolean value (True or False).
#Return True if the amount of x's and o's are the same.
#Return False if they aren't the same amount.
#The string can contain any character.
#When "x" and "o" are not in the string, return True.

def XO(s):
    x=0;o=0
    for y in s:
        if y.lower()=="x":
            x+=1
        elif y.lower()=="o":
            o+=1
        else:
            continue
    return (x==o)


# In[12]:


XO("zpzpzpp")


# In[13]:


#5 Create a function that reverses a boolean value and returns the string "boolean expected" if another variable
#type is given.

def reverse(a):
    if type(a)==bool:
        return not(a)
    else:
        return "boolean expected"


# In[14]:


reverse(True) 


# In[15]:


#6 Using list comprehensions, create a function that finds all even numbers from 1 to the given number.

def find_even_nums(n):
    l=[]
    for x in range(1,n+1):
        if x%2==0:
            l.append(x)
        else:
            continue
    return l


# In[16]:


find_even_nums(10)


# In[17]:


#7 Create a function that takes a list of strings and integers, and filters out the list so that it returns a 
#list of integers only.

def filter_list(lst):
    l=[]
    for x in lst:
        if type(x)==int:
            l.append(x)
        else:
            continue
    return l


# In[18]:


filter_list([4, 2, 3, "ab", "ef", 4])


# In[19]:


#8 Write a function that takes a list and a number as arguments. Add the number to the end of the list, then 
#remove the first element of the list. The function should then return the updated list.

def next_in_line(l,n):
    if len(l)>0:
        l.append(n)
        l.pop(0)
        return l
    else:
        return "No list has been selected"


# In[20]:


next_in_line([5, 6, 7, 8, 9], 1)


# In[21]:


#9 In BlackJack, cards are counted with -1, 0, 1 values:
#2, 3, 4, 5, 6 are counted as +1
#7, 8, 9 are counted as 0
#10, J, Q, K, A are counted as -1
#Create a function that counts the number and returns it from the list of cards provided.

def count(lst):
    c=0
    for x in lst:
        if x==10 or x=="J" or x=="Q" or x=="K" or x=="A":
            c+=-1
        elif x>=2 and x<=6:
            c+=1
        else:
            continue
    return c


# In[22]:


count([5, 9, 10, 3, "J", "A", 4, 8, 5])


# In[23]:


#10 Wild Roger is participating in a Western Showdown, meaning he has to draw (pull out and shoot) his gun faster 
#than his opponent in a gun standoff. Given two strings,p1 and p2, return which person drew their gun the fastest.
#If both are drawn at the same time, return "tie".

def showdown(p1,p2):
    if p1.lower().find("b")>p2.lower().find("b"):
        return "p2"
    elif p1.lower().find("b")<p2.lower().find("b"):
        return "p1"
    else:
        return "Tie"


# In[24]:


#13 Create a function that takes a number as an argument and returns True or False depending on whether the number
#is symmetrical or not. A number is symmetrical when it is the same as its reverse.

def is_symmetrical(n):
    num=str(n)
    return num==num[::-1]


# In[26]:


is_symmetrical(121)


# In[27]:


#13 Write a function that returns the strings:
#"both" if both given booleans a and b are True.
#"first" if only a is True.
#"second" if only b is True .
#"neither" if both a and b are False.

def True_or_False(a,b):
    if a==True and b==True:
        return "both"
    elif a==True:
        return "first"
    elif b==True:
        return "second"
    else:
        return "neither"


# In[28]:


#14 I'm trying to watch some lectures to study for my next exam but I keep getting distracted by meme compilations,
#vine compilations, anime, and more on my favorite video platform.Your job is to help me create a function that
#takes a string and checks to see if it contains the following words or phrases:
#"anime"
#"meme"
#"vines"
#"roasts"
#"Danny DeVito"
#If it does, return "NO!". Otherwise, return "Safe watching!".

def prevent_distractions(strin):
    x=strin.lower()
    l=x.split()
    c=0
    for s in l:
        if s=="anime" or s=="meme" or s=="vines" or s=="roasts" or s=="danny" or s=="devito":
            c+=1
        else:
            continue
    if c>0:
        return "NO!"
    else:
        return "Safe watching!"


# In[29]:


prevent_distractions("How to ace BC Calculus in 5 Easy Steps")


# In[30]:


#15 Create a function that takes three integer arguments (a, b, c) and returns the amount of integers which are of
#equal value.

def equal(a,b,c):
    if a==b==c:
        return 3
    elif a==b or b==c or c==a:
        return 2
    else:
        return 0


# In[31]:


equal(2, 2, 2)


# In[32]:


#16 Create a function which validates whether a 3 character string is a vowel sandwich. In order to have a valid 
#sandwich, the string must satisfy the following rules:
#The first and last characters must be a consonant.
#The character in the middle must be a vowel.

def is_vowel_sandwich(s):
    v=0;c=0
    if len(s)==3:
        for x in s:
            if x=="a" or x=="e" or x=="i" or x=="o" or x=="u":
                v+=1
            else:
                c+=1
        return (c==2 and v==1)
    else:
        return False


# In[33]:


#17 Write a function that takes a string, breaks it up and returns it with vowels first, consonants second. 
#For any character that's not a vowel (like special characters or spaces), treat them like consonants.

def split(z):
    v="";c=""
    for y in range(len(z)):
        if z[y]=="a" or z[y]=="e" or z[y]=="i" or z[y]=="o" or z[y]=="u" or z[y]=="A" or z[y]=="E" or z[y]=="I" or z[y]=="O" or z[y]=="U":
            v+=z[y]
        else:
            c+=z[y]
    return (v+c)


# In[34]:


#18 Write a function that takes a string and calculates the number of letters and digits within it. 
#Return the result in a dictionary.

def count_all(s):
    d={}
    l=0;n=0
    for x in s:
        if x.isalpha():
            l+=1
        elif x.isdigit():
            n+=1
        else:
            continue
    d.update({"LETTERS":l,"DIGITS":n})
    return d


# In[35]:


#19 Write a function that returns the boolean True if the given two lists do not share any numbers, and False 
#otherwise.

def is_list_same(l1,l2):
    for x in l1:
        if x in l2:
            return False
    return True


# In[36]:


is_list_same([1,2,3],[4,5])


# In[38]:


#20 Lists can be mixed with various types. Your task for this challenge is to sum all the number elements in 
#the given list. Create a function that takes a list and returns the sum of all numbers in the list.

def numbers_sum(l):
    s=0
    for x in l:
        if type(x)==int:
            s+=x
        else:
            continue
    return s


# In[39]:


numbers_sum([1, 2, "13", "4", "645"])


# In[40]:


#32 Write a function that returns True if the given positive integer is a prime number and False if it's not.

def is_prime(i):
    a=0
    for x in range(1,i+1):
        if i%x==0:
            a+=1
        else:
            continue
    if a==2:
        return True
    else:
        return False


# In[41]:


is_prime(2)


# In[42]:


#33 Create a function that takes a string s and returns a list of two-paired characters. If the string has an 
#odd number of characters, add an asterisk * in the final pair.

def string_pairs(s):
    l=[]
    for x in range(0,len(s),2):
        if x==len(s)-1:
            l.append(s[x]+"*")
        else:
            l.append(s[x]+s[x+1])
    return l


# In[43]:


string_pairs("Hareesh")


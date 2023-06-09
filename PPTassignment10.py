#!/usr/bin/env python
# coding: utf-8

# In[1]:


#answer 1

def power(n):
    return n > 0 and 3 ** round(math.log(n , 3)) == n


# In[2]:


import math


# In[3]:


print(power(27))


# In[4]:


print(power(9))


# In[5]:


print(power(45))


# In[6]:


print(power(0))


# In[7]:


print(power(-1))


# In[8]:


#Answer 2

def remaining(n):
    return 1 if n == 1 else 2 * (n // 2 + 1 - remaining(n // 2))


# In[9]:


print(remaining(9))


# In[10]:


print(remaining(1))


# In[18]:


#Answer 3 .


def printSubsets(s, current="", index=0):
    if index == len(s):
        print(current)
        return

    printSubsets(s, current, index + 1)
    printSubsets(s, current + s[index], index + 1)


# Example usage
printSubsets("abc")
printSubsets("abcd")


# In[19]:


#answer 4.


def Lenght(s):
    if s == "":
        return 0
    else:
        return 1 + Lenght(s[1:])
    


# In[20]:


string = "abcd"
lenght = Lenght(string)
print(lenght)


# In[23]:


#Answer 5.

def strings(s):
    count = 0
    n = len(s)
    
    for i in range(n):
        count += 1
        left = i - 1
        right = i + 1
        
        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
            
        left = i - 1
        right = i + 1
        while left >= 0 and right < n and s[left]  == s[right]:
            count += 1
            left -=1
            right += 1
            
    return count

string = "abcad"
count = strings(string)
print(count)


# In[35]:


#Answer 6.

def townofHanoi(n, source, destination, auxiliary):
    if n == 1:
        print("move disk 1 from rod", source, "to rod", destination)
        return 1
    
    moves = 0
    
    moves += townofHanoi(n -1, source, auxiliary, destination)
    print("Move disk", n, "from rod", source, "to rod", destination)
    moves += 1
    moves += townofHanoi(n -1, auxiliary, destination , source)
    return moves

N = 2
total = townofHanoi(N, 1, 3, 2)
print(total)


# In[36]:


N = 3
total = townofHanoi(N , 1, 3, 2)
print(total)


# In[37]:


#Answer 7.

def permute(s, l, r):
    if l == r:
        print(''.join(s))
    else:
        for i in range(1, r + 1):
            s[l], s[i], = s[i], s[l]
            permute(s, l + 1 , r)
            s[l], s[i] = s[i], s[l]


# In[40]:


def printPermutations(str):
    n = len(str)
    s = list(str)
    permute(s, 0, n -1)


# In[42]:


str = "cd"
printPermutations(str)


# In[43]:


#Answer 8.

def consonants(string):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    count = 0
    for char in string:
        if char in consonants:
            count += 1
    return count


# In[44]:


input = "abc de"
result = consonants(input)
print(result)


# In[45]:


input = "geeksforgeeks portal"
result = consonants(input)
print(result)


# In[ ]:


`


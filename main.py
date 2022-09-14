#!/usr/bin/env python
# coding: utf-8
#jocelyn's code
# # Objectives Week 4
# 
#name = input("what is your name?")
#print(name)



#string manipulations
text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#substring???
fragment = text[::3]
print(fragment.lower())

#spliting strings
text2 = "we are learning about splitting strings"
print(len(text2))
#split allows us to split strings into different 
#characters or words
print(text2.split())
splitText = text2.split()
print(splitText[4])



# 1. Understand lists in python programming, 
# 2. list functions, 
# 3. tuples, 
# 4. methods and functions,
# 5. if statements and comparisons in **python** **bold text**
# 6. by the end of the week, you will learn to develop a text parser, a program that the user will enter any kind of text and the code will give them any information about that text: you will have to learn the index method, extracting sub-strings, methods and properties of string.
# ## copy this to your own drive

# # First lets go over simpler index methods
# 

# In[ ]:


#we know the traditional way. You might find this way annoying. 
#There are several other ways you can format or insert variables into string texts
#lets take a look at indexing in python again


# ![image.png](attachment:image.png)

# In[3]:


#print your result


# In[7]:


#lets take a look at substrings


# In[ ]:





# # Lists

# In[ ]:


#Lists allow you to store multiple items in one variable instead of separate items
#now you are entering the world of data structures
#lists are known as arrays in other programs
#python calls arrays lists --> they are like a book shelf of items
#List are ordered sequences that can hold a variety of object types
#They use [] brackets and commas to separate objects in a the list
#[1,2,3,4,5]
#List support indexing and slicing. Lists can be nested and also have a variety of useful methods that can be called off of them.#


# In[ ]:


apples = 3
oranges = 4
grapes = 50
mangos = 5
#list
groceries = [apples, oranges, grapes, mangos]
print(groceries)
print(groceries[-1])


# In[1]:


#CREATE  A LIST OF FRIENDS AND print out the 1st and last friend
friends = []

#lists are mutable -- means I can change it


# In[2]:


birthday_guests = ["femi", "will", "luis"]
Christmas_guests =["hou", "jessie","Tom"]

#joins my list 
#concatenation
newList = birthday_guests + Christmas_guests
print(newList)
print(newList.remove("Tom"))
print(newList)
newList.append("Rebecca")
newList.append("Jose")
newList.append("James")
print(newList)
print(newList.sort())
print(len(newList))





##!/usr/bin/env python
# coding: utf-8
#jocelyn's code
# # Objectives Week 4
# 
# name = input("what is your name?")
# print(name)


# 1. Understand lists in python programming, 
# 2. list functions, 
school_list = ["notebook", "pen"]
# 3. tuples, 
# 4. methods and functions,
# 5. if statements and comparisons in **python** **bold text**
# 6. by the end of the week, you will learn to develop a text parser, a program that the user will enter any kind of text and the code will give them any information about that text: you will have to learn the index method, extracting sub-strings, methods and properties of string.
# ## copy this to your own drive
avengers = ["hawkeye", "hulk", "iron man", "black panther", "captamer"]
multiDimen =[[3,5], [7,6], [6,3], [8,9]]
print(multiDimen[0][0])
#multidimensions arrays are more than just
#a single list of items
# # First lets go over simpler index methods
# 

# In[ ]:


#we know the traditional way. You might find this way annoying. 
#There are several other ways you can format or insert variables into string texts
#lets take a look at indexing in python again


# ![image.png](attachment:image.png)

# In[3]:


#print your result


# In[7]:


#lets take a look at substrings


# In[ ]:





# # Lists

# In[ ]:


#Lists allow you to store multiple items in one variable instead of separate items
#now you are entering the world of data structures
#lists are known as arrays in other programs
#python calls arrays lists --> they are like a book shelf of items
#List are ordered sequences that can hold a variety of object types
#They use [] brackets and commas to separate objects in a the list
#[1,2,3,4,5]
#List support indexing and slicing. Lists can be nested and also have a variety of useful methods that can be called off of them.#


# In[ ]:


apples = 3
oranges = 4
grapes = 50
mangos = 5
#list
groceries = [apples, oranges, grapes, mangos]
print(groceries)
print(groceries[-1])


# In[1]:


#CREATE  A LIST OF FRIENDS AND print out the 1st and last friend
friends = []

#lists are mutable -- means I can change it


# In[2]:


birthday_guests = ["femi", "will", "luis"]
Christmas_guests =["hou", "jessie","Tom"]

#joins my list 
#concatenation
newList = birthday_guests + Christmas_guests
print(newList)

#remove
print
# birthday_guests[0] ="charlie"


# add

#sort


#.remove(), .append(), sort(), .len() are list functions


# In[3]:


#also we can define N dimensional list not just 1 dimensional
#1 dimensional means only one item per comma


# In[ ]:





# In[ ]:


#create a list that contains at least one string, one integer and one float
#for example: [1, "two", 3.14566]
#Note that the order and number of items doesnt matter


# # List functions

# In[ ]:


#how do we recognize a function????

#.remove()


# In[ ]:


#.append()


# In[ ]:


#.pop()


# In[ ]:


#.sort()
#.reverse()


# In[2]:


#.insert(index, value)


# In[ ]:


#.index(value)


# In[ ]:


#.extend()


# In[ ]:


#.copy()


# #Tuples

# In[ ]:


# exactly the same thing as an array only it is immutable, once you define the tuple, you cannot change it


# In[1]:


#you define a tuple with () instead of [] like you would in lists
#once you define it, you cannot change it
#example
coordinates = (4,5)


# #Functions and methods

# In[ ]:





# #return statement

# In[ ]:





# #if statements

# ![image.png](attachment:image.png)

# #if statements and comparisons

# In[ ]:





# In[ ]:





# # #challenge --- building a better calculator

# In[ ]:





# In[ ]:





# 


#remove
# birthday_guests[0] ="charlie"


# add

#sort


#.remove(), .append(), sort(), .len() are list functions


# In[3]:


#also we can define N dimensional list not just 1 dimensional
#1 dimensional means only one item per comma


# In[ ]:





# In[ ]:


#create a list that contains at least one string, one integer and one float
#for example: [1, "two", 3.14566]
#Note that the order and number of items doesnt matter


# # List functions

# In[ ]:


#how do we recognize a function????

#.remove()


# In[ ]:


#.append()


# In[ ]:


#.pop()


# In[ ]:


#.sort()
#.reverse()


# In[2]:


#.insert(index, value)


# In[ ]:


#.index(value)


# In[ ]:


#.extend()


# In[ ]:


#.copy()


# #Tuples

# In[ ]:


# exactly the same thing as an array only it is immutable, once you define the tuple, you cannot change it


# In[1]:


#you define a tuple with () instead of [] like you would in lists
#once you define it, you cannot change it
#example
coordinates = (4,5)


# #Functions and methods

# In[ ]:





# #return statement

# In[ ]:





# #if statements

# ![image.png](attachment:image.png)

# #if statements and comparisons

# In[ ]:





# In[ ]:





# # #challenge --- building a better calculator

# In[ ]:





# In[ ]:





# 
#lets take a look at substrings




########################################################################################################################
# 3 challenges
#exercises for index method
#1  Find and display on the screen which character occupies the fifth position within the following word:

# "computer"




#2 Find and display the index of the first occurrence of the word "practice" in the following sentence:



# "In theory, theory and practice are the same. In practice, they are not."






#3 Find and display the index of the last occurrence of the word "practice" in the following sentence:



# "In theory, theory and practice are the same. In practice, they are not."


########################################################################################################################

#extracting substrings
# Take every third character starting from the ninth to the end of the sentence, and print the result.



# "Never trust a computer you can't throw out a window"

# Reverse the position of all the characters in the following sentence and displays the result on the screen.



# "It's great to work with computers. They don't argue, they remember everything and they don't drink your beer"


########################################################################################################################

#more challenges
# Print the following text in uppercase, using the specific string method:



# "Especially in electronic communications, writing in all caps is equivalent to yelling."

# Join the following list into a string, separating each item with a space. Use the appropriate list/string method, and display the result.
# word_list = ["Simple","is","better","than","complex."]



# Replace in the following sentence:

# "If the implementation is hard to explain, it might be a bad idea."

# the following pairs of words:

# "hard" --> "easy"

# "bad" --> "good"

# and display the sentence with both words modified.

########################################################################################################################



#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Practice


# In[1]:


2+2


# In[2]:


print(2+2)


# In[3]:


print("Hello World")


# In[4]:


print("hello world",2+2,"this is me")


# In[6]:


print("hello world",2+2,"this is me",sep=" ")


# In[ ]:


#comment


# In[7]:


print("hello"+"world")


# In[10]:


print("hello" + " world")


# In[11]:


#Variables


# In[12]:


price=900
print("The value of phone is $",price,sep="")


# In[13]:


is_billed = True
print(is_billed)


# In[14]:


type(price)


# In[ ]:


#operations


# In[17]:


price = 900
discount = 15
price_after_discount = price - discount
print("The price of the iphone after the doiscount is $", price_after_discount, sep="")


# In[ ]:


#type conversion -- Implicit & Explicit


# In[ ]:


#Lists & Tuples in python


# In[18]:


Brand = "Apple"
print(Brand)


# In[19]:


#Creating a list
brand_list=["Apple","LG","Apple"]
brand_list


# In[20]:


type(brand_list)


# In[21]:


#len function for count of elements inside a list.
len(brand_list)


# In[ ]:


#min & max func


# In[ ]:


# Printing the third item in the list ram_list : indexing(in python indexing starts with 0)


# In[22]:


print(brand_list[2])


# In[23]:


print(brand_list[0:2])


# In[24]:


print(brand_list[-1])


# In[25]:


# Remove the last element from the list brand_list
brand_list.pop()


# In[26]:


# insert the element through "append"
brand_list.append("Motorola")


# In[27]:


brand_list


# In[ ]:


#Tuples :  immuatble variables
#Difference between tuple and lists is that unlike lists we can not changenthe elements of a tuple once it is assigned.


# In[ ]:


#Dictionaries in python : 
#if we want to store the more attributes , more info then we use dictionaries


# In[29]:


#creating the dictionary
attributes = {
    "Brand" : "Apple",
    "RAM" : 4,
    "Storage" : 125,
    "Price" : 800,
}
print(attributes)


# In[ ]:


#dictionaries are used to store data values in key:value pairs, written in curly bracket


# In[ ]:


#Conditional statements :


# In[ ]:


# is else statement in python
if (test expression):
    body of if
else:
    body of else


# In[31]:


print(price)


# In[32]:


#define the budget price
budget = int(input("Enter your budget(in dollars): "))

# if else statement
if price <= budget:
    print("Congrats! You can buy the Iphone")
else:
    print("Sorry! the mobile price is more than your budget")


# In[ ]:


if there are multiple conditions , then go with if-elif-else statement
syntax:

if(test expression):
    body of if
elif(test expression):
    body of elif
else:
    body of else


# In[34]:


Memory = int(input("ENter the memory:"))

if Memory == 32:
    print("The price of the phone is $600")
elif Memory == 64:
    print("The price of the phone is $700")
elif Memory == 128:
    print("The price of the phone is $900")
else:
    print("Please enter a valid memory requirement")


# In[ ]:


#Looping statements in python


# In[40]:


#range
print(range(6))
print(list(range(6)))
print(list(range(2,6)))
print(list(range(2,14,2)))


# In[ ]:


#loops are used in python to iterate over a sequence,


# In[ ]:


for iterator_var in sequence:
    statement(s)


# In[44]:


price=900
for i in range(5,21,5):
    discount = price*(i/100)
    discounted_price = price - discount
    print(
        "The prices after providing ",i," percent discount is $",discounted_price,sep="",
    )


# In[ ]:


#While condition:
    statements(s)


# In[46]:


price = 900
i=5
while i<=20:
    discount = price * (i/100)
    discounted_price = price - discount
    print(
        "The price after providing ",i," percent discount is $",discounted_price,sep="",
    )
    i+=5


# In[49]:


# list comprehensions in python
price_list = [900, 899, 600, 1000]
discounted_price_list = [x - (x*(5/100)) for x in price_list]
print(discounted_price_list)


# In[ ]:


#asking for custmer budget
#budget = int(input("Enter your budget(in dollars): "))
#within_budget = ["Yes" if x <= budget else "No" for x in discounted_price_list]
#price(within_budget)


# In[ ]:


budget = [900, 899, 600, 1000]
discounted_price_list=[855.0, 854.05, 570.0, 950.0]

within_budget = []
for x discounted_price_list:
    if x <= budget:
        within_budget.append("Yes")
    else:
        within_budget.append("No")
print(within_budget)


# ### Functions in python 

# In[ ]:


#Syntax of a function 
def function_name(parameters):
    '''expalin what a function does'''
    statement(s)


# In[ ]:


#Write s func for display of attributes of iphone

def display_iphone_attributes():
    """"
    This func displays
    the stored attributes of
    the apple iphone
    """"
    price=900
    ram=4
    stroage=128
    
    print(
    "The apple iphone has ",
    ram,
    "GB Ram and",
    storage,
    "GB internal stroage and cost $",
    price,
    sep="",
    )


# In[ ]:


display_iphone_attributes()


# In[ ]:


def display_phone_attributes(brand,price,ram,storage):
    """"
    This function displays
    the stored attributes of
    and phone
    """"
    
    print(
    "The ",
    brand,
    " phone has",
    ram,
    "GB RAM and",
    stroage,
    "GB internal stroage and it costs $",
    price,
    sep="",
    )


# In[ ]:


display_phone_attributes("sam",899,90,23)


# In[ ]:


#lambda function
dis_price_lambda = lambda discount:900-(900*(discount /100))


# In[ ]:


dis_price_lambda(10)


# In[ ]:


#Args and Kwargs in python 
pyhton allows us flexiblity in terms of the number of arguments passed to a function by using *args


# In[ ]:


positional arguments and keyword arguments
"args" hepls us remove the constants on the number of positional arguments
"kwargs" arguments passed while calling the function must be a mapping , such as a dictionary.


# In[ ]:





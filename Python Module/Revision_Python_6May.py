#!/usr/bin/env python
# coding: utf-8

# ### OOPs Concepts

# In[1]:


# Creating a empty Class
class Mobile:
    pass


# In[2]:


#created class mobile
class mobile:
  brandname = "Apple"
# created object "obj"
obj = mobile()
#printing the mobile name using object
print(f"Mobile Name:{obj.brandname}")


# In[3]:


#it is clearly seen that self and obj is
#referring to the same object
class find:
	def __init__(self):
		print("Address of self in Python = ",id(self))
obj1 = find()
print("Address of class object in Python= ",id(obj1))


# In[4]:


class mobile:
    def __init__(self, brandname, price):
        self.brandname = brandname
        self.price = price
    def say_hi(self):
        print(f"Hi, the mobile brand is {self.brandname} and its costs {self.price} rupees.")
mobile1 = mobile("Samsung", 30000)
mobile1.say_hi()


# In[6]:


#Classmethod in built parameter
class college:
    course='BE'
    def opted(obj):
        print("Chosen course : ",obj.course)
college.opted = classmethod(college.opted)
college.opted()


# In[7]:


#create class method using classmethod
class employee:
    empname = "Ram"
    def print_empname(obj):
        print("The employee name is : ",obj.empname)
employee.print_empname = classmethod(employee.print_empname)
employee.print_empname()


# ### Constructors and Destructors 

# In[8]:


#Default constructor
class employee:
    def __init__(self):
        self.empname = "Tarun"
    def print_empname(self):
        print(self.empname)
obj = employee()
obj.print_empname()
            


# In[9]:


#paramterized constructors
class Product:
    number1 = 0
    number2 = 0
    product = 0
    def __init__(self,n1,n2):
        self.number1 = n1
        self.number2 = n2
    def display(self):
        print("Enter first number =" + str(self.number1))
        print("Enter Second number =" + str(self.number2))
        print("Product of two number =" + str(self.product))
    def calc(self):
        self.product = self.number1 * self.number2
obj1 = Product(1000,2000)
obj2 = Product(10,20)
obj1.calc()
obj2.calc()
obj1.display()
obj2.display()


# ### Destructors

# In[10]:


class Student:
    def __init__(self):
        print('Student created')
    def __del__(self):
        print('Destructor was called hence student deleted')
obj = Student()
del obj


# In[11]:


class student:
    def __init__(self,stuname):
        self.stuname = stuname
    def say_hello(self):
        print('Hello, my name is',self.stuname)
p = student('James')
p.say_hello()


# In[12]:


class Bike:
    bikename = ""
    bikegear = 0
bike1 = Bike()
bike1.bikegear = 5
bike1.bikename = "Royal Enfield"
print(f"Name:{bike1.bikename},Gears:{bike1.bikegear}")


# In[ ]:





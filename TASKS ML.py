#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Խնդիր 1

n = int(input("Մուտքագրեք թիվ: "))
if n % 2 == 0:
    print(f"{n} թիվը զույգ է։ ")
else: 
    print(f"{n} թիվը կենտ է։ ")


# In[2]:


#Խնդիր 2

n = int(input("Մուտքագրեք բնական թիվ։ "))
gumar = 0
for i in range (n + 1):
    gumar += i 
print(gumar)


# In[4]:


#Խնդիր 3

def findlargestone(numbers):
    
    if not numbers:
        return None
    
    largest_number = numbers[0]
    for i in numbers:
        if i > largest_number:
            largest_number = i
            
    return largest_number
    
my_list = [23, 45, 67, 12, 89, 34]
largestnum = findlargestone(my_list)
print(f"Շարքի ամենամեծ թիվը՝ {largestnum}-ն է։")


# In[9]:


#Խնդիր 4

def fibonacci(n):
    fib_list = [1, 1]
    for i in range(2, n):
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list[:n]

fib = fibonacci(0)
print(fib) 


# In[6]:


#Խնդիր 5

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, money):
        self.balance += money
    def withdraw(self, money):
        if self.balance >= money:
            self.balance -= money
        else:
            print("Անբավարար միջոցներ։")  
    def get_balance(self):
        return self.balance
    
account = BankAccount('15689416396', 7000.0)
account.deposit(500.0)
account.withdraw(300.0)
print(account.get_balance ())


### datatypes________________
num1 = 100
print(type(num1))
num2 = 15.45
print(type(num2))
st = "string"
print(st, type(st))
l = [1,2,3,4,5]
l.append("string")
print(l, type(l))
t = (11,22,33)
print(t, type(t))
dict = {"name":"ABC", "email":"abc@efg.com"}
print(dict, type(dict))
set = {11,22,33}
print(set, type(set))
# bool: True False
# complex: 4 + 3j
print(3 in l)
print(17 in t)
print("name" not in dict)


### operators________________
# arithmetic: +,-,*,/,//,%,**
# comparitive: <,>,<=,>=,==,!=
# identity: is is not
# assignment: =,+=,-=,*=,/=
# bitwise: &,|,^,>>,<<
# logistic: and,or,not
# membership: in, not in


### conditional statements_______
num11 = 100
num22 = 200
if num11 > num2:
    print("num11 is greater")
elif num1 < num2:
    print("num2 is greater")
else:
    print("num1 and num2 are equal")


### loops________________ 
l = [10,20,30,40,50]
sum = 0
for value in l:
    sum = sum + value
    print(sum)
range(5)
range(2,11)
range(2,11,2)
for value1 in range(1,21):
    sum = sum + value1
print(sum)
# break
# continue
# enumerate
l = [10,20,30,40,50,60]
key = 40
for value in l:
    if value == key:
        print("Element found: ", value)
        break
    else:
        continue
        print("Statement after continue")
        # won't print because of continue
else:
    print("Element not found")

for index,value in enumerate(l):
    print(index,value)      
key = 40

for index,value in enumerate(l):
    if value == key:
        print("Element found ", value, "at index ",index)
        break
    else:
        pass
        # print("Statement after continue")
        # will print every interation
else:
    print("Element not found")

# while loop
count = 1
sum = 0
while count <= 20:
    sum = sum + count
    count = count + 1
print(sum)
# for loop preferred when iterate over specific range
# while loop when specific condition


###strings________________
s = "Python string"
print(type(s))
# indexing
print(s[4])
# slicing
print(s[7:])
# stride
print(s[::-2]) #starts from last, jumps 2
for value in s[::2]:
    print(value) 
# functions for strings
print(dir(str))
num1 = 100
num2 = 200
print("value of num1 is {}, value of num2 is {}".format(num1,num2))
print("value of num2 is {1}, value of num1 is {0}".format(num1,num2))
print("value of num2 is {val2}, value of num1 is {val1}".format(val1=num1,val2=num2))
s = "upper"
s1 = s.capitalize()
# id(s) location stays so defining new variable
print(s1)
print(s)
print(s.upper())
print(s.lower())
print(s.title())
print(s.isupper())
print(s.islower())
# split, join
s = "HTML,CSS,PYTHON,JAVA,Django"
l = s.split(",") 
print(l)
s1 = (" ").join(l)
print(s1)
# maketrans
# translate
s1 = "abcd"
s2 = "1234"
s3 = "python sample string abcd "
table = str.maketrans(s1,s2)
result = s3.translate(table)
print(result)
# index
# find
# rfind function
s = "HTML,CSS,PYTHON"
print("PYTHON" in s)
print(s.index("PYTHON"))
# starting index
s = "HTML,CSS,PYTHON,PYTHON"
print(s.find("python"))
# find("PYTHON") will give 9 like index()
# python gives -1
# find from right side
print(s.rfind("PYTHON"))
s = "        sample            "
s1 = s.strip(" ")
print(s1)
s = "python"
s1 = s.center(20,"*")
print(s1)
s1 = s.rjust(20,"*")
print(s1)
s = "HTML,CSS,PYTHON,PYTHON"
s1 = s.replace("HTML","html")
print(s1)


###tuples________________
t = (10,20,30,40)
print(t,type(t))
print(t[:3])
t = (10,20,20,20,30,30,40)
print(t.index(20))
print(t.index(30))
print(t.count(20))
l = [10,20,30,40,50]
for index,value in enumerate(l):
    print(index,value)
for x in enumerate(l):
    print(x[1])
t = tuple(l)
print(t)    
t = ("a","b","c",100)
l = list(t)
print(l, type(l))    


###lists________________
l = [10,20,30,40,"python",[100,200,300]]
print(l,type(l))
# indexing and slicing
print(l[-1][1])
print(l[::-1])
l = [100,200,300,400,500]
for value in l[::2]:
    print(value)
print(id(l))
l.append(600)
print(id(l)) #same location
num1 = 100
print(id(num1))
print(id(l[0])) #location is for values
l.extend([600,700])
print(l)
l.append([600,700])
print(l)
# can't l.append([600,700],800)
l.extend("python")
print(l)
l.insert(1,1000) 
print(l) 
l = [10,20,30]
l2 = l
print(l,l2)
print(id(l))
print(id(l2)) #same because locaiton of values
l.insert(0,100)
print(id(l))
l = [10,20,30,40,50]
r = l.pop() #automatically last
print(l,r)
l.remove(20)
print(l) 
l = [50,40,20,30,10]
print(l.sort()) #or sorterd()
print(l[::-1])
l.reverse()
print(l)
l2 = [100,200,300]
print(l+l2)


###dictionary________________
d = {"id":101,
     "name":"ABC",
     "email":"abc@efg.com"}
print(d)
d["number"] = 9178424094
print(d)
d["number"] = 9178532532
print(d)
print(d["id"])
# print(d[0]) error because of no key O
print(d.get("number"))
print(d.get("date"))
print(d.get("date","key doesn't exist"))
for key in d:
    print(key,d[key])
d = {}
for value in range(1,11):
    d[value] = value * value
print(d)
print(d.keys())
print(d.values())
print(d.items())
for t in d.items():
    print(t)
l1 = [1,2,3,4,5]
l2 = [1,4,9,16,25]
d = dict(zip(l1,l2))
print(d)
d1 = {1:1,2:3,3:9,4:16}
d2 = {5:25,6:36}
d1.update(d2)
print(d1)
r = d1.pop(3)
print(d1,r) #r show popped key
r = d1.popitem()
print(d1,r) #shows popped key and value
d1.clear() #clear every element
del d1 #error if already cleared


###set________________
s = {10,20,30,40,50}
print(s,type(s))
s = {10,20,30,20,40,20,50}
print(s,type(s)) # elements unique
s = {100,200,300,400}
s.add(500)
print(s)
s1 = {10,20,30,40,50,60}
s2 = {40,50,60,70,80,90}
s3 = s1.union(s2)
print(s3)
s3 = s1.intersection(s2)
print(s3)
s3 = s1.difference(s2)
print(s3)
s3 = s2.difference(s1)
print(s3)
s3 = s1.symmetric_difference(s2)
print(s3)
print(s1)
s1.update(s2)
print(s1)
s1.intersection_update(s2)
print(s1)
# s1.difference_update(s2)
# print(s1)
print(s2.issubset(s1)) #if all s2 in s1
print(s2.issuperset(s1)) #s2 superset of s1
l1 = [1,2,3,4]
s1 = set(l)
print(s)
l2 = [5,2,4,6,7,8,15]
s2 = set(l2)
s3 = s1.union(s2)
print(s3)
l3 = list(s3)
l3 = sorted(l3)
print(l3)
# can't pop(), can remove(), discard() same as remove() but won't give error if not found


###math,random module________________
import math
l = [0.1] * 10
print(sum(l))
print(math.fsum(l))
num = 15.556
print(math.floor(num),math.ceil(num))
# math.sqrt(), factorial()
d,i = math.modf(num)
print(d,i)
print(math.pow(10,2))
print(math.log(10))
print(math.log10(2))
print(math.log2(10))
print(math.sin(0))
print(math.sin(90)) #degrees
print(math.sin(math.radians(90))) 
print(math.cos(math.radians(90))) 
print(math.tan(math.radians(90))) 
import random
print(random.random()) #b/w 0 to 1
l = [1,2,3,4,5]
print(random.choice(l))
print(random.randint(1,3)) #1,2,3
print(random.randrange(1,3)) #1,2
print(random.uniform(10,20)) #float


###def, functions________________
s = "Python,HTML,CSS"
print(s.index("HTML"))
def value_reverse(value):
    reverse = value[::-1]
    #print(reverse)
    return reverse
s = "Python"
result = value_reverse(s)
print(result) #None, result already calculated
l = [10,20,30,40]
l.append(50)
print(l.append(50)) #None, only modifying list 
result = value_reverse(l)
print(result)
num = 100
result = value_reverse(num) #int error
def value_reverse(value):
    if type(value)==list or type(value)==str:
        reverse = value[::-1]
    else:
        temp = str(value)
        reverse = temp[::-1]
    return reverse
result = value_reverse(num)
print(result)
# positional argument
def linear_search(l,key):
    for value in l:
        if key == value:
            return True
    else:
        return False
l = [100,200,300,400]
key = 500
result = linear_search(l,key)
print(result)
# default argument
print(ord('a')) #returns unicode point
print(chr(97)) #returns unicode character
print(ord('a'),ord('z')) #97-122
print(ord('A'),ord('Z'))  #65-90
print(chr(1),chr(50),chr(200)) #special characters
# 8 char, 1 Upper, 1 lower, 1 special, 5 digits
import random
def gen_password(length=8):
    l = ['.',',','!','@','#','$']         
    upper = chr(random.randint(65,90))
    lower = chr(random.randint(97,122))
    special = random.choice(l)
    digit = random.randint(10000,99999)
    password = upper + lower + special + str(digit)
    l = random.sample(password,length)
    password = ("".join(l))
    return password
result = gen_password()
print(result)
# keyword argument
def validate(username,password):
    if username=="ABC" and password=="Abc@123":
        print("valid password")
    else:
        print("invalid password")
validate("ABC","Abc@123")         
validate(password="Abc@123",username="ABC")         
print(100,200,sep=",",end=" ") #default=100 200 ; Hi
print("Hi") #100,200 Hi
# variable length positional args
l = [100,200,300,400]
l.append[500,250,350] #error
def add_value(*args):   # * converts to tuple
    l = []
    for value in args:
        l.append(value)    
    return l
result = add_value(100,200,300,400,500)
print(result)
result = add_value(100,200,300,400,500,600,700,800)
print(result)
# variable length keyword args
# name,email,contact,dob
def get_details(**kwargs): # ** converts to dict    
    print(kwargs)
get_details(name="ABC", email="abc@gmail.com", contact=9171112222, dob="10-21-2050")
get_details(name="ABC", email="abc@gmail.com", dob="10-21-2050")
get_details(name="ABC", email="abc@gmail.com")
# recursive functions
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)
num = 5
result = factorial(num)
print(result)                        
# binary search
def binary_search(l,key):
    if len(l) == 0:
        return False
    else: 
        mid = len(l) // 2 
        if l[mid] == key:
            return True
        elif key < l[mid]:
            return binary_search(l[:mid],key)
        else: 
            return binary_search(l[mid+1:],key)        
print(__name__) #__main__
if __name__ == "__main__":   
    l = [100,200,300,400,500,600,700,800,900]
    key = 100
    result = binary_search(l,key)
    # mid = 9/2 = 4 = 500 > 700 
    # [600,700,800,900]
    # mid = 4/2 = 2 = 800 < 700
    # [600,700]
    # mid = 2/2 = 1 = 700 == 700 return True
    print(result)
# SAVE mod1.py 
import mod1
l = [100,200,300,400,500]
key = 5000
print(mod1(l,key))
help(mod1)
""" (beginning of script, shows under NAME)
Description
Author      
Date 
"""
""" (under def, shows under FUNCTIONS)
Binary search: input list and key
return True if ___ else return False
"""
###__init__.py will be considered a python directory


###list comprehension_________________
l = [100,200,300,400,500]
l2 = [value*value for value in l]
print(l2)
for value in l:
    l2.append(value*value)
print(l2)
l = [10,20,30,40,50,60,70,85]
l2 = [value for value in l if value%2 == 0]
print(l2)
l = ["abc","abcd","abcde","zzzzzz"]
l2 = [len(value) for value in l]
print(l2)
l2 = [(value1,value2) for value1 in range(1,5) for value2 in range(100,103)]
print(l2)
l = [[1,2,3],[4,5,6],[7,8,9]]
l2= []
for value in l:
    for value2 in value:
        l2.append(value2)
print(l2)
l2 = [value2 for value in l for value2 in value]
print(l2)
# even, odd
l = [100,105,110,115,120]
l2 = ["even" if value%2 == 0 else "odd" for value in l]
print(l2)
# squares dict
d = {x:x**2 for x in range(1,11)}
print(d)
d = {chr(x):x for x in range(97,123)}
print(d)
d2 = {key:value for value,key in d.items()}
print(d2)


###map, filter, lambda________________
def sqr(num1):
    return num1**2
l = [10,20,30,40,50,60]
result = list(map(sqr,l))
print(result)
# map(cube, range(1, 11))
# [cube(1), cube(2), ..., cube(10)]
def add(num1,num2):
    return num1+num2
l1 = [100,200,300,400,500]
l2 = [10,20,30,40,50]
result = list(map(add,l1,l2))
print(result)
def check_num(num1):
    if num1%2 == 0:
        return True
    else:
        return 0
l = [100,115,120,130,140]
result = list(filter(check_num,l)) #filter True 
print(result)
# filter(f, range(2, 25))
# result = []
# for i in range(2, 25):
#    if f(i):
#        result.append(i)
l = [10,20,30,40,50,60]
result = list(map(lambda num1:num1**2,l))
print(result)
l = [100,115,120,130,140]
result = list(filter(lambda num:num%2==0,l))
print(result)
d = {8:50,3:40,2:30,4:20,5:20}
l = sorted(d.items()) #sorts key
print(l)    
l = dict(sorted(d.items(),key=lambda x:x[1])) #sorts value
print(l) 
   

###generators______________________
def printVal(l):
    for value in l:
        print(value)
l = [10,20,30,40,50,60]
printVal(l)
def fibo():
    first_num = 0
    second_num = 1
    yield second_num
    while(True):
        next_val = first_num + second_num
        yield next_val
        first_num,second_num = second_num,next_val
g = fibo()
print(g)
print(next(g)) #1
print(next(g)) #2
print(next(g)) #3
print(next(g)) #5
for value in range(10):
    print(next(g))
for value in range(5): #next 5 after 10
    print(next(g))
def printVal(l):
    for value in l:
        #print(value) #all
        #return value #only last
        yield value #all 
l = [10,20,30,40,50,60]
g = printVal(l)
print(next(g)) #10
print(next(g)) #20...
l = [10,20,30,40,50,60]
l2 = [value * value for value in l] #list
l2 = (value * value for value in l) #generator object
print(next(l2)) #100
print(next(l2)) #400
# generating only once and processing > processing everytime


###regulse expressions________________
import re 
# . - any char
# [a-zA-Z] - char class
# [0-9] - digit class
# + - atleast one; [a-z]+
# * - zero or more
# ^ - start of string
# $ - end of string
# ? - optional
# [a-z]{2,4} - 2 min 4 max occurences of character
s = "ABCDE1234A"
r = re.compile("[A-Z]{5}[0-9]{4}[A-Z]")
l = re.findall(r,s)
print(l)
s = "AAAAAAABCDE1234A"
r = re.compile("^[A-Z]{5}[0-9]{4}[A-Z]")
l = re.findall(r,s)
print(l) 
s = "ABCDE1234AAAAAAA"
r = re.compile("^[A-Z]{5}[0-9]{4}[A-Z]$")
l = re.findall(r,s)
print(l)
s = "12-05-2018"
r = re.compile("^[0-9]{2}-[0-9]{2}-[0-9]{4}$")
l = re.findall(r,s)
print(l)
s = "12-05-2018"
r = re.compile("^([0-9]{2})-([0-9]{2})-([0-9]{4})$")
m = re.search(r,s)
if m:
    print(m.group(2)) #05
else: 
    print("pattern not found")
s = "12-05-2018"
r = re.compile("^(?P<date>[0-9]{2})-(?P<month>[0-9]{2})-(?P<year>[0-9]{4})$")
m = re.search(r,s)
if m:
    print(m.group("year")) #2018
else: 
    print("pattern not found")
s = "+91 8123456789"
r = re.compile("(?:\+91\s)?([6-9][0-9]{9})")
m = re.search(r,s)
if m:
    print(m.group(1)) #9 digit num 
else: 
    print("pattern not found")
# space \s
# [0-9] \d 
# [^0-9] \D     everything but 0-9 
# [a-zA-Z] \w


###web scrapping____________________    
# pip install requests
# pip install BeautifulSoup
import requests 
from bs4 import BeautifulSoup
response = requests.get("https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Residential-House,Villa&cityName=Vadodara")
print(response)
print(response.content) 
print(response.status_code) #200 to start scraping
soup = BeautifulSoup(response.content,"html.parser")
print(soup)
print(soup.prettify())
cards = soup.find("div",attrs={"class":"m-srp-card__container"})
# get attrs from content
print(cards) 
for card in cards:
    price = card.find("div",attrs={"class":"m-srp-card__price"})
    print(price.text)
    title = card.find("span",attrs={"class":"m-srp-card__title__bhk"})
    print(title.text.strip("\n")) #strips empty line 
    carpet_area = card.find("div",attrs={"class":"m-srp-card__summary__info"})
    print(carpet_area.text)
    data = "{}{}{}".format(title.text.strip("\n"),price.text,carpet_text.text)
    print(data)


###object oriented___________________ 
class Account: 
    def __init__(self,cust_id,name,initial_bal=0):
        self.id = cust_id
        self.name = name
        self.balance = initial_bal
    def get_balance(self):
        return self.balance
    def deposit(self,amount):
        self.balance = self.balance + amount
        return self.balance
    def withdraw(self,amount):
        if amount > self.balance:
            return "insufficient balance"
        else:
            self.balance -= amount
            return self.balance
customer1 = Account("101","ABC")
# Account(customer1,"101","ABC")
print(customer1.id,customer1.name,customer1.balance) #101 ABC 0
print(customer1.get_balance()) #0
print(customer1.deposit(5000)) 
print(customer1.id,customer1.name,customer1.balance) 
customer2 = Account("102","XYZ")
customer2.deposit(40000)
customer1.withdraw(5000)
print(customer2.id,customer2.name,customer2.balance) 
customer3 = Account("103","PQR")
#print("c3 balance: ", customer3.balance)
customer3.deposit(20000) 
customer2.withdraw(50000) #insufficient balance
print(customer3.id,customer3.name,customer3.balance) 
customer4 = Account("104","EFG")
customer4.deposit(100000)
# iterate
l = [customer1,customer2,customer3,customer4]
for obj in l:
    if obj.balance < 10000:
        print(obj.id,obj.name)
# can do self.__balance in def so can't access it outside of class
# can access it using obj.get_balance()
# or print(customer1._Account__balance)
# or print(customer1.__dict__)
class account:
    count = 0    
    @classmethod
    def incr_count(cls):
        cls.count += 1
    @classmethod
    def get_count(cls):
        return cls.count
    @staticmethod
    def print_val():
        print("static method in account class")
    def __init__(self,cust_id,name,initial_bal=0):
        self.__id = cust_id
        self.__name = name
        self.__balance = initial_bal
        #account.count += 1
        account.incr_count()
    def get_balance(self):
        return self.__balance
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def deposit(self,amount):
        self.balance = self.balance + amount
        return self.__balance
    def withdraw(self,amount):
        if amount > self.__balance:
            return "insufficient balance"
        else:
            self.__balance -= amount
            return self.__balance
customer1 = account("101","ABC")
customer2 = account("102","XYZ")
customer3 = account("103","PQR")
customer4 = account("104","EFG")
print(account.count) #4
# class acount's count 4 so shows 4 for all its objects
print(customer1.count) #4
customer1.count = 100 #created variable count in customer1 
print(customer1.count) #100
account.count += 5 #9
print(account.__dict__) 
print(customer1.__dict__)
print(account.get_count()) #every object created
account.print_val()
# inheritance
class saving_account(Account): #account __access
    def __init__(self,id,name,initial_bal=0):
        super().__init__(id,name,initial_bal) #call existing method: super()
        self.limit = 50000
    def withdraw(self,amount):
        if amount < self.limit:
            new_bal = super().withdraw(amount)
            self.limit -= amount
            return new_bal
        else:
            print("daily limit reached")
cust1 = saving_account(101,"ABC")
print(cust1.__dict__)
#help(cust1) #method resolution order: saving_account, account, builtins.object, or error
print(cust1.deposit(80000))
print(cust1.withdraw(10000)) #first searches in child class, if not then parent class
print(cust1.withdraw(70000)) #limit
# multiple inheritence
class A:
    pass
class B:
    pass
class C(A,B):
    pass
obj = C()
help(obj)
# method order: depth, left, right approach- C,A,B


###sqlite
import sqlite3
conn = sqlite3.connect("example1.db")
c = conn.cursor()
#c.execute("""CREATE TABLE IF NOT EXISTS EMP(ID INT PRIMARY KEY,NAME TEXT,SALARY REAL)""")
#c.execute("INSERT INTO EMP(ID,NAME,SALARY) VALUES(101,'ABC',80000)") 
#c.execute("INSERT INTO EMP(ID,NAME,SALARY) VALUES(101,'XYZ',70000)") #UNIQUE contraint failed
#c.execute("INSERT INTO EMP(ID,NAME,SALARY) VALUES(101,'PQR',45000)")
#c.execute("INSERT INTO EMP(ID,NAME,SALARY) VALUES(101,'EFG',35000)")
#conn.execute("COMMIT")
c.execute("""SELECT * FROM EMP""")
#for row in c:
#    print(row)
c.execute("UPDATE EMP SET SALARY = 65000 WHERE ID = 102")
#conn.execute("COMMIT")    
c.execute("SELECT * FROM EMP WHERE ID = 102")
print(next(c))
c.execute("""DELETE FROM EMP WHERE ID = 103""")
conn.execute("COMMIT")
c.execute("""SELECT * FROM EMP""")
for row in c:
    print(row) #(101, 'ABC', 80000.0)


###iterators and itertools__________
l = [100,200,300,400,500]
i = iter(l)
print(i)
for value in i:
    print(value)
import itertools
l1 = [10,20,30,40,50]
l2 = [100,200,300,400,500]
l3 = [1000,2000,3000,4000,5000]
i = itertools.chain(l1,l2,l3)
l = [100,200,300,400,500]
print(next(i))
for value in i:
    print(value)
l = [100,200,300,400,500]
count = 0
for value in itertools.cycle(l):
    if count < 10:
        print(value)
    else:
        break
    count += 1
l = [10,20,30,40,50]
count = 0
for value in itertools.repeat(l):
    if count < 10:
        print(value)
    else:
        break
    count += 1
l = [10,20,30,40]
i = iter(l)
t = itertools.tee(i,5)
i = itertools.chain(l1,l2,l3)
for value in itertools.islice(i,0,8):
    print(value)
count = 0
for value in itertools.count(10,5): #starts at 10, increments of 5
    if count > 20:
        break
    else:
        print(value)
    count += 1
l = [1,2,3]
print(list(itertools.permutations(l,2)))  
print(list(itertools.combinations(l,2)))  


###decorators_____________________  
def deco(func):
    def new_func(val1,val2):
        if type(val1)==type(val2):
            return func(val1,val2)
        else:
            return func(str(val1),str(val2))
    return new_func
@deco
def concat(val1,val2):
    return val1 + val2
result = concat(10,10)
print(result)
result = concat("python","string")
print(result)


###input, output
my_file = open("output.txt", "r+") #read and write
my_list = [i ** 2 for i in range(1, 11)]
my_file = open("output.txt", "w")
my_list = [i ** 2 for i in range(1, 11)]
my_file = open("output.txt", "w")
for value in my_list:
    my_file.write(str(value) + "\n")  
my_file.close()
my_file = open("output.txt", "r") #read only
print(my_file.read())
my_file.close()
my_file = open("text.txt", "r")
print(my_file.readline(),my_file.readline(),my_file.readline()) #\n in readlines()
print(my_file.readline()) #an extra \n after last print
my_file.close()
write_file = open("text.txt", "w")
read_file = open("text.txt", "r")
write_file.write("Not closing files is VERY BAD.")
write_file.close()
print(read_file.read())
read_file.close()
r = open("text.txt","r")
with open("text.txt", "w") as textfile:
  textfile.write("Success!")
print(r.read())
with open("text.txt", "w") as my_file:
  my_file.write("My Data!")  
if not my_file.closed:
  my_file.close()
print(my_file.closed)


################################################################################
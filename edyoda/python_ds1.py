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
    sum1 = sum1 + value1
print(sum1)
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
print(s.find("python))
# find("PYTHON") will give 9 like index()
# python gives -1
# find from right side
print(s.rfind("PYTHON))
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



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


###strings___________________
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
 
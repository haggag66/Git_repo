# to move to console you write (`python`)
# intrudational information
# from typing import List#it as library name "List"










speed = 60
print(speed)#output:60
speed =20.5
a,b,c=4,2,'hello'
a=b='welcome'
print(speed)#output:20.5
IsOpen=True
IsMoveing=False
print(IsOpen)#True
print(IsMoveing)#False

# format and compine with string and integer

name='Mohamed Haggag'
name=name + ' '+'is web developer'
print(name)#output:Mohamed Haggag is web developer
date='{}/{}/{}'.format('1','mars',2019)#format is function to put values inside {} by orderly
print(date)#output:1/mars/2019
test='from {0} to {1}'.format("earth","mars")
print(test)#output:from earth to mars
test='from {1} to {1}'.format("earth","mars")
print(test)#output:from mars to mars
speedCar='speed of car:{:d}, speed allow:{:d}'.format(60,50)
# if you want put in {integer},you use {:d}(d is refer to integer)
# if you want put in {float}, you use {:f}(:f is refer to float )
# if you want put in {string}, you use {:s}(:s is refer to strnig)
print(speedCar)#output:speed of car:60, speed allow:50

# List
myList=[1,2,'hi',3.5,True]#List
names=['ali','mohamed','adel','salma','tota']
print(names)#output:['ali', 'mohamed', 'adel', 'salma', 'tota']
print(names[0])#output:ali
names.append('haggag')# it used to add element to list but it will add in the end of the list
print(names)#output:['ali', 'mohamed', 'adel', 'salma', 'tota', 'haggag']
names.insert(3,'abdo')# it used to add element to list but you enter its position the element in the list
print(names)#output:['ali', 'mohamed', 'adel', 'abdo', 'salma', 'tota', 'haggag']
names.insert(2,'abdo')
print(names)#output:['ali', 'mohamed', 'abdo', 'adel', 'abdo', 'salma', 'tota', 'haggag']
print(names.count('abdo'))#output:2
#it used to know that the count of element 
names.remove('abdo')# it used to remove the first element have as same as value from the list
print(names)#output:['ali', 'mohamed', 'adel', 'abdo', 'salma', 'tota', 'haggag']
names.remove('abdo')
print(names)#output:['ali', 'mohamed', 'adel', 'salma', 'tota', 'haggag']
names.reverse()# it used to reverse elements in the list
print(names)#output:['haggag', 'tota', 'salma', 'adel', 'mohamed', 'ali']
names.sort()# it used to sort elements in the list
print(names)#output:['adel', 'ali', 'haggag', 'mohamed', 'salma', 'tota']
numbers=[1,2,3,11,4,3,78,56]
print(numbers)#output:[1, 2, 3, 11, 4, 3, 78, 56]
numbers.sort()# it used to sort elements in the list
print(numbers)#output:[1, 2, 3, 3, 4, 11, 56, 78]
Name='haggag'
print(Name[0])#output:h
print(Name[2])#output:g

namelist=list(Name)#it used to convert string to static list
print(namelist)#output:['h', 'a', 'g', 'g', 'a', 'g']

# dictionaries
amountInBank = {'haggag':30, 'mohamed':50, 'salma':40, 'tota':60}#amountInBank={key:value,key:value}
print(amountInBank['haggag'])#output:30
amountInBank['adel']=90
print(amountInBank)#output:{'haggag': 30, 'mohamed': 50, 'salma': 40, 'tota': 60, 'adel': 90}
amountInBank['salma']=80
print(amountInBank)#{'haggag': 30, 'mohamed': 50, 'salma': 80, 'tota': 60, 'adel': 90}
del amountInBank['salma']#it used to delete key and element from dictionaries
print(amountInBank)#output:{'haggag': 30, 'mohamed': 50, 'tota': 60, 'adel': 90}
print('salma' in amountInBank)#output:False
# `in` it used to check if the key exists in the dictionary
print(amountInBank.keys())#output:dict_keys(['haggag', 'mohamed', 'tota', 'adel'])
# `keys()` it used to know what are keys in the dictionary
print(amountInBank.values())#output:dict_values([30, 50, 60, 90])
amountInBank.pop('haggag')#it used to delete key from dictionaries
print(amountInBank)#output:{'mohamed': 50, 'tota': 60, 'adel': 90}
# amountInBank.clear()  #it used to delete all keys in the dictionary#
print(list(amountInBank.keys()))
#`List(`dictionary.method()`)` it used to convert a dictionary to a list
print(amountInBank.get('mohamed'))#output:50
# it used to get the value for a key in the dictionary


# operations
print(2+4)#output:6
print(3-2)#output:1
print(5*4)#output:20
print(12/4)#output:3.0
print(13/4)#output:3.25
print(13%4)#output:1
a=10
a+=1
print(a)
print(4>2)#True
print(5<2)#False
print(5<=5)#True
print(20==8)#False
print(20!=8)#True
print('a'>'b')#False
Mylist=[1,4,6,2,1,3,'moon']
print(1 in Mylist)#True
print('a' in 'apple')#True
print('m' is 'moon')#False  is `==`
print(1 not in Mylist)#False
print('m' is not 'moon')#True  is not `!=`
# you should know where put not (if it with is ,it will put after is // if it with in ,it will put before in)
print(5>3 and 5==5)#True
print(5<2 and 9==9)#False
print(5<2 and 9==3)#False
print(5<2 or 9==9)#True
print(5>2 or 9==4)#True
print(5<2 or 9==5)#False
print(not(32>93))#False


# conditional
age=13
if age<18:
    print(f"Your age is {age} you should wait for the next year.")
    
age=20
if age>=18 and age<=60:
    print("you can drive a car yourself")
elif age>=18 and age>60:
    print("your can drive a car yourself and you are very old")
"you are very youner to drive a car yourself"if age<18 else"you can drive a car yourself"


# looping
age=12
while age<18:
    print(f"you wait for the next year because your age is {age}")
    age+=1
ages=[21,12,15,18,25,17,13]
for age in ages:
    print(age)
for index,age in enumerate(ages):
    print(f"{index} is {age} ")
people={'mohamed':40,'haggag':35,'adel':30,'mona':17}
for i in people:
    print(i)#`print(people[i].keys())`
for i in people.items():
    print(i)#`print(people[i])`
for k,v in people.items():
    print(k)#k is people.keys()
    print(v)#v is people.value()
for k,v in people.items():
    if v>=18:
        print(f'{k} you can drive a car yourself')
    else:
        print(f"{k} you can't drive a car yourself")

# functions
def subTwoNumber():
    number=3-1
    print(number)

def addTwoNumber(num1,num2):
    number=num1+num2
    print(number)

def multiplyTwoNumber(num1=1,num2=1):
    number=num1*num2
    print(number)
def divideTwoNumber(num1=1,num2=1):
    number=num1/num2
    return number
subTwoNumber()
addTwoNumber(3,2)
# addTwoNumber() `error` because you must send parameters to function 
multiplyTwoNumber()
number=divideTwoNumber(3,2)
print(number)
number=divideTwoNumber(num1=2,num2=4)
print(number)
number=divideTwoNumber(num2=2,num1=4)# you can change parameter location when you call function
print(number)
# function's parameter
def my_function(*args,**kwargs):
    print(args)# *args:it call the list in the function
    print(kwargs)# **kwargs: it call dictionary in function
my_function()
my_function(20,15,name="my_function")
def my_function2(*args,**kwargs):
    for i in  args:
        print(i)
    for i in kwargs:
        print(i+' '+str(kwargs[i]))
my_function2(20,15,name="my_function2")






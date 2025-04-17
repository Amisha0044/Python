############################################
# FUNCTIONS
# - create function for each task in a big project, so that it can be reused again
############################################
'''
def greet():
    print("Hello!")

def add_sub(a,b):
    return a+b, a-b

# greet()
add, sub = add_sub(5,3)
print("sum = ",add,"\n","\bsubtraction = ",sub)


##############################################
# FUNCTION ARGUMENTS
##############################################

def update(x):
    print(id(x))        # 140727082878152
    x=8
    print(x)            # 8
a=10
print(id(a))            # 140727082878152
update(a)               # 8 - looks like pass by value since int is immutable
print(a)                # 10

def update_list(listt):
    print(id(listt))    # 1820241077760
    listt[2]=60
    print(listt)        # [2, 4, 60]
lt = [2,4,6]
print(id(lt))           # 1820241077760
update_list(lt)         # [2, 4, 60] - looks like pass by reference since list is mutable
print(lt)               # [2, 4, 60]

# Python neither has pass by value not pass by reference.
# In Python...
# All variables are passed by object reference — but:
# ~ If it's immutable, it behaves like pass by value
# ~ If it's mutable, it behaves like pass by reference

def person(name,age=18):          # FORMAL ARGUMENTS -- default argument
    print('{} is of {} years'.format(name,age))

person("navin",35)     # ACTUAL ARGUMENTS -- position arguments-- navin is of 35 years
person(45,"kiran")     # 45 is of kiran years
person(name="navin",age=35)       # keyword arguments--  navin is of 35 years
person("shweta")                  # shweta is of 18 years


def summ(*b):                    # variable length argument - can have any number of args
    print(b)
    print(sum(b))                # sum of tuple b

summ()                           # () ; 0
summ(2)                          # (2,)  ;   2
summ(2,4)                    # (2, 4)    :   6
summ(1,2,3,4,5)              # (1, 2, 3, 4, 5)   ;   15

# OR
def summa(a, *b):
    print(a)# variable length argument - can have any number of args
    print(b)
    res = a
    for tuple_item in b:
        res = res + tuple_item
    print(res)

summa(2,4)                    # 2 ;   (4,)    ;   6
summa(1,2,3,4,5)              # 1 ;   (2, 3, 4, 5)    ;   15


# KEYWORDED VARIABLE LENGTH ARGUMENTS (kwargs)

def person1(name, *data):       # variable length args: *data
    print(name)                 # navin
    print(data)                 # (35, 'mumbai', 6575975646)

def person2(name, **data):      # keyworded variable length args (kwargs): **data [usually we use **kwargs (recommended), but we can use any name like **data]
    print(name)                 # navin
    print(data)                 # {'age': 35, 'city': 'mumbai', 'mobile': 6575975646}
    for k,v in data.items():
        print(k,":",v)

person1("navin",35, 'mumbai', 6575975646)
person2("navin",age=35, city='mumbai', mobile=6575975646)


# GLOBAL VS. LOCAL VARIABLES
# "global" KEYWORD, "globals()" FUNCTION

a=10
aa=5
def something():
    a=20

    global aa
    aa=55

    aa =110         # but it is global as already declared with global keyword, but what if we want it to be local as welll in the same function?: use "globals()" function
    # b=100
    print("a inside function: ", a)
    # print("b inside function: ", b)

# something()                             # a inside function:  20    ;   b inside function:  100
something()                             # a inside function:  20
print(a)                                # 10
# print(b)                              # NameError: name 'b' is not defined
print(aa)                               # 55


a=10
b=20
c=30
print(id(a))            # 140727067739336

def concept():
    x = globals()       # returns all the global variables
    print(x)            # {'__name__': '__main__', ..., '__file__': 'C:\\Users\\Amisha Sharma\\Documents\\Python\\Python-Telusko-YT\\5_functions.py', '__cached__': None, 'a': 10, 'b': 20, 'c': 30, 'concept': <function concept at 0x00000231D8E2F240>}
    y = globals()['a']  # y is referencing the global variable 'a'
    print(y)            # 10
    print(id(y))        # 140727067739336 -- global var
    # y=100     # doesn't work
    globals()['a'] = 101        # updating global variable's value from 10 to 101

    a=1
    print('in function: ',a)    # in function:  1
    print(id(a))        # 140727067739048 -- local var

concept()
print(a)                # 101



# PASSING LIST TO A FUNCTION

def list_operation(lst):
    even, odd = 0, 0
    for item in lst:
        if item%2==0:
            even += 1
        else:
            odd += 1
    return even,odd

n=int(input("enter length of list: "))
lt=[]
for i in range(n):
    lt.append(int(input("enter your list elements: ")))

even, odd = list_operation(lt)
print("even nums = ",even, "\nodd nums = ",odd)


def names_length_check(lst):
    count=0
    for name in lst:
        if len(name)>5:
            count += 1
    return count;

n=int(input("enter length of list: "))
lt=[]
for i in range(n):
    b=input("enter name: ")
    lt.append(b)

count = names_length_check(lt)
print("Number of people having name length>5 = {}".format(count))



##########################################
# RECURSION
##########################################

import sys

print(sys.getrecursionlimit())      # to view to recursion limit, by default is 1000 in python to avoid software hang issue

i=0
def greeting():
    global i
    i += 1
    print("Hello", i)
    greeting()

# greeting()
sys.setrecursionlimit(2000)         # to set the recursion limit, here 2000 times is the limit
greeting()



#####################################################
# ANONYMOUS FUNCTION (LAMBDA FUNCTION)
#####################################################

def square(a):
    return a*a

num = int(input("enter a number: "))

result = square(num)
print(result)

sqr = lambda a : a*a      # 1 line of code, instead of 2 lines
result = sqr(num)
print(result)

add = lambda a,b : a+b
result = add(5,4)
print(result)
'''
from functools import reduce

# def is_even(number):
#     return number%2==0
# def do_double(number):
#     return number*2
# def add_all(a,b):
#     return a+b

nums = [3,2,6,8,4,6,2,9]
# print(filter(lambda n : n%2==0, nums))          # <filter object at 0x0000019CBC35ABC0>

# evens = list(filter(is_even, nums))
evens = list(filter(lambda n : n%2==0, nums))   # using lambda function instead of normal function to make it more efficient and since it's a custom function, needed only once
print(evens)                                    # [2, 6, 8, 4, 6, 2]

# double = list(map(do_double,evens))
double = list(map(lambda n : n*2, evens))
# print(map(lambda n : n*2, evens))               # <map object at 0x00000298173FB700>
print(double)                                   # [4, 12, 16, 8, 12, 4]

# sum = reduce(add_all, double)
sum = reduce(lambda a,b : a+b, double)
print(sum)                                      # 56


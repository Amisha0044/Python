############################################
# DECORATORS
############################################

'''
def div(a,b):
    print (a/b)


def smart_div(func):

    def inner(a,b):     # same number of args as div()
        if a<b:
            a,b = b,a
        return func(a,b)

    return inner


division = smart_div(div)   # smart_div() function takes a function "div()" as its argument
division(2,4)
'''

def greet(func):
    def modified_func(*args, **kwargs):
        print("good day..")
        func(*args, **kwargs)
        print("Thanks for using the function..")
    return modified_func

@greet
def hello():
    print("Hello User!!!")

@greet
def add(a,b):
    print("sum = ", a+b)

hello()
add(3,6)
# greet(hello)()      # traditional/alternative way if not using line# 31 and 35
# greet(add)(3,6)

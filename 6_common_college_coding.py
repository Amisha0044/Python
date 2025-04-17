# FIBONACCI SERIES
# 0 1 1 2 3 5 8 13 21 34 ...
'''
def fibonacci(n):
    a,b = 0,1
    if n<=0:
        print("please enter a limit that is greater than 0!")
    elif n==1:
        print(a,end=' ')
    else:
        print(a,end=' ')    # n=1
        print(b,end=' ')    # n=2
        for i in range(3,n+1):  # n= 3 to n
            sum = a + b
            print(sum,end=' ')

            a=b
            b=sum

n=int(input("enter limit: "))
fibonacci(n)


# if user give n=100, means the end limit is 100, so all fib num before 100
def fibonacci(n):
    a,b = 0,1
    sum=a+b
    if n<0:
        print("please enter a limit that is positive!")
    elif n==0:
        print(a,end=' ')
    else:
        print(a,end=' ')    # n=1
        print(b,end=' ')    # n=2
        # for i in range(3,n+1):  # n= 3 to n (n=1: n=3 to 2 - doesn't go into loop)
        #     sum = a + b
        #     if sum<=n:
        #         print(sum,end=' ')
        #         a=b
        #         b=sum
        while sum<=n:
            print(sum, end=' ')
            a=b
            b=sum
            sum=a+b

n=int(input("enter end limit: "))
fibonacci(n)



# FACTORIAL OF A GIVEN NUMBER

def factorial(num):
    fact=1;
    for i in range(1,num+1,1):
        fact = fact*i
    if num<0:
        return "please enter a positive number!"
    elif num==0:
        return 1
    else:
        return fact

num= int(input("enter a number: "))
result = factorial(num)
print(result)
'''


# FACTORIAL USING RECURSION

def fact(num):
    if num==0:
        return 1
    else:
        return num*fact(num-1)

num=int(input("enter a number: "))
res=fact(num)
print(res)


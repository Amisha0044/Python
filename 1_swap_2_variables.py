# swap 2 variables using 3rd variable
a,b = 3,56

t=a
a=b
b=t
print("a=",a,"\nb=",b)


# swap two variables without using 3rd variable
a,b = 3,56

a = a+b     # 59
b = a-b     # 3
a = a-b     # 56
# print("a="+a+"\nb="+b)      # error
print("a=",a,"\nb=",b)


# optimized way in python
a,b = 6,11

a,b = b,a
print("a=",a,"\nb=",b)
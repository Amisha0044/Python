'''
#################################################
# CONDITIONAL STATEMENTS
###################################################

if True:
    print('I am right')

################################
if False:
    print('I am wrong')
print('Bye')

################################
num=int(input("Enter a number: "))
rem=num%2
if rem==0:
    print("Even")
if rem==1:
    print("Odd")
print('Bye')
# not optimized code as checking both the condition, if one condition is satisfied then other condition will not.

# multiple if are used for independent conditions, to check all if conditions.
# if else is used for dependent conditions, if condition true, then execute, otherwise execute else part.

###############################
# nested if - if inside the if
num=int(input("Enter a number: "))
rem=num%2
if rem==0:
    print("Even")
    if num>5:
        print("even num is greater than 5")
else:
    print("Odd")
print('Bye')

###############################
# if - elif - else
num=2
if num==1:
    print("one")
elif num==2:        # it will come to this only if above condition is false
    print("two")
else:               # it will come to this only if above conditions are false
    print("wrong input")



################################################
# LOOPS - to do repetitive tasks; to execute similar or logically similar statements number of times.
# while loop, for loop
################################################

# WHILE LOOP - widely used for condition based iteration

i=1                     # initialization
while i<=5:             # condition check
    print("Telusko")
    i=i+1               # increment/decrement

i=5
while i>=1:
    print("reverse loop")
    i=i-1

i=1
while i<=5:
    print("Telusko", end=" ")
    j=1
    while j<=3:
        print("rocks", end=", ")
        j=j+1
    print()
    i=i+1


# FOR LOOP - widely used with sequences (list, string etc.)

listt = ['navin',65,2.5]
for i in listt:
    print(i)

stringg = "NAVIN"
for i in stringg:
    print(i)

for i in {1,3,5,7}:
    print(i)

for i in range(5):
    print(i)

for i in range(1,5,2):
    print(i)

for i in range(5,0,-1):
    print(i)

for i in range(1,10):
    if i%5!=0:
        print(i)



# BREAK & CONTINUE

candies_available = 5
candies_bought = int(input("Hey user, enter number of candies you want to buy: "))

while candies_bought>0:
    if candies_bought>candies_available:
        print("candies out of stock, please try with less candies count")
        break
    print("machine is giving a candy")
    candies_bought-=1

print("Thanks for purchase, have a great day!")


candies_available = 5
candies_bought = int(input("Hey user, enter number of candies you want to buy: "))

count=1;
while count<=candies_bought:
    if count>candies_available:
        print("candies out of stock now")
        break
    print("machine is giving a candy")
    count+=1

print("Thanks for purchase, have a great day!")


for i in range(11):
    if i%3==0:
        continue
    print(i)
print("bye")


# printing even numbers from 0 to 10
for i in range(11):
    if i%2!=0:      # checking if odd numbers
        pass
    else:
        print(i)
print("bye")

# printing odd numbers from 0 to 10
for i in range(11):
    if i%2!=0:      # checking if odd numbers
        pass
        print(i)
print("bye")

# printing all numbers from 0 to 10
for i in range(11):
    if i%2!=0:      # checking if odd numbers
        pass
    print(i)
print("bye")


def fun():
    print("do something")
fun()

def fun():
    # indentation error if no code in the body, hence put pass to avoid any error when no code is needed
    pass
fun()



# PRINTING PATTERNs

# # # #
# # # #
# # # #
# # # #

str = "# "
for i in range(0,4):
    print(str * 4)

for j in range(4):
    for i in range(4):
        print("# ", end="")
    print()


#
# #
# # #
# # # #

str = "# "
for i in range(1,5):
    print(str*i)

for i in range(1,5):            # i represents no. of rows
    for j in range(1,i+1):      # j represents no. of columns
        print("# ", end="")
    print()


# # # #
# # #
# #
#

str = "# "
for i in range(4,0,-1):
    print(str*i)

for i in range(5,0,-1):       # i represents no. of rows
    for j in range(1,i):      # j represents no. of columns
        print("# ", end="")
    print()

for i in range(4):
    for j in range(4-i):
        print("# ", end="")
    print()



# FOR ELSE - works only if "if" has "break", then only "else" can be used with "for" loop.
nums = [4,158,67,88,251]
for num in nums:
    if num%5==0:
        # print(num+"found")    # TypeError: unsupported operand type(s) for +: 'int' and 'str'
        print(num, " found")
        break
else:
    print("not found")



# FIND IF GIVEN NUMBER IS PRIME (Prime is a number which is divisible only by 1 and the number itself) OR NOT

num = int(input("Enter a number: "))
count=0
for i in range(2,num):
    if num%i==0:
        count+=1
        break
if count==0 and num!=1:
    print("prime number")
elif num==1:
    print("neither prime nor composite number")
else:
    print("not a prime number")


num = int(input("Enter a number: "))
for i in range(2,(num//2)+1):           # more efficient
    if num%i==0:
        print("not a prime number")
        break
else:
    print("prime number")
'''


###########################################################
# ITERATOR & GENERATOR
#
# - used to iterate
# - iterator preserves the state i.e. last value
#
# - how to create an iterator object of built-in sequence: itr = iter(nums)
# - how to get next value in iterator object:
#   * way-1: print(itr.__next__())
#   * way-2: print(next(itr))
#
# - we use iterator to fetch one value at a time
#   Ex. we have list of 100 elements but we want to access elements one by one, one element at a time - use iterator is recommended
#
# - disadv: we need to create iterator by ourselves, using 2 methods: iter() and next()
#
# - solution to disadv: use GENERATORS, generator creates iterator for us.
#
# why to use generator?
# - if you want to fetch 1000 records to process, you can use generator to process one record at a time, so that only one value gets loaded to memory at a time instead of loading whole list of 1000 records into memory at once.
###########################################################

'''
nums = [7,8,9,5]

print(nums[0])          # 7
print(nums[-1])         # 5
# print(nums[6])          # IndexError: list index out of range

for i in nums:
    print(i)            # 7 ; 8 ; 9 ; 5

# 1st way
itr1 = iter(nums)       # iterator preserves the state i.e. last value
print(itr1)              # <list_iterator object at 0x000001F9C51BAC80> -- printing the object of iterator
print(itr1.__next__())   # 7
print(itr1.__next__())   # 8
print(itr1.__next__())   # 9
print(itr1.__next__())   # 5
# print(itr1.__next__())   # StopIteration (Exception) - program terminated as ec=xception is not being handled
print("checking...")

# 2nd way
itr2 = iter(nums)
print(next(itr2))       # 7

for i in nums:
    print(i)            # 7 ; 8 ; 9; 5

# iterator shown above works for built-in data types like list, tuple etc.

# How to create/implement your own iterator? -- ex. below class
class Top10:
    def __init__(self):
        self.num=1

    # iter() will give you object of iterator
    # next() will give you the next value/object
    def __iter__(self):
        return self
    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

obj = Top10()

print(next(obj))    # 1

for i in obj:
    print(i)        # 2 ; 3 ; 4 ; 5 ; 6 ; 7 ; 8 ; 9 ; 10 ; bye

print("bye")


# generator function - generates an iterator for us
def top10():
    yield 1         # yield is a special keyword that will make your function a generator
    yield 2         # it is similar to return but return terminates the function but yield doesn't
    yield 3

val = top10()
print(val)          # <generator object top10 at 0x000001CEA7E55D20> -- object of iterator
print(next(val))    # 1
# print(next(val))    # StopIteration

for i in val:
    print(i)        # 2 ; 3



def top10_square():
    n=1
    while n<=10:
        sq = n*n
        yield sq
        n += 1

val = top10_square()    # calling the top10_square() function

for i in val:
    print(i)        # 1; 4; 9; 16; 25; 36; 49; 64; 81; 100

# why to use generator?
# - if you want to fetch 1000 records to process, you can use generator to process one record at a time, so that only one value gets loaded to memory at a time instead of loading whole list of 1000 records into memory at once.
'''


###############################################################
# EXCEPTION HANDLING in PYTHON
#
# Errors:
# 1) compile-time error -
#   - checked and occurs at compile time
#   - syntactical error: ex. missing : , spelling mistake
# 2) logical error
#   - occurs at runtime
#   - at developer side, checked during testing
#   - 2+3 = 5 you are getting and not 4 i.e. bugs
# 3) run-time error
#   - checked and occurs at runtime
#   - at user end or due to connection issue
#   - code compiled successfully, no logical error, but error occurred because of user, not your fault
#   - ex. input error, 6/0, file not found error, db and internet/network connection error
#
# Exception:
# - An error because of which the normal flow of program gets terminated
# Exception handling:
# - Even if you're getting error, program execution should not be stopped and should continue as usual.
#
###############################################################


a=5             # normal statement - will not give any error
b=2
# b=0

try:            # try to execute this block; if any error, raise exception, which has to be excepted by except block
    print("resource open")
    print(a/b)      # critical statement - where we can get error, possibility of error
    # 2.5   ;   bye
    # ZeroDivisionError: division by zero
    k = int(input("enter a number: "))
    print(k)
    # print("resource closed")    # won't be executed if exception is raised

except ZeroDivisionError as e:
    print("hey, you can't divide a number by zero! - ", e)
except ValueError as e:
    print("invalid input!")
except Exception as e:  # except block only gets executed if try block raises any exception
    # e is the representation of an object of Exception
    print("oops, something went wrong!")

finally:        # finally block will be executed if we get error as well as if we don't get the error
    print("resource closed")

print("bye")

# if you open a file, you should close the file; if you open a db connection, close it.
# so, whatever resource you open, close it after you are done.


#####################################
# ARRAY IN PYTHON
#####################################
'''
# import array          # need to use array.array()
from array import *     # arrray() works

values = array('i',[5,9,-8,4,2])        # 1D array
print(values)

print(values.buffer_info())     # returns (address, size);      a method
print(values.typecode)          # returns the type code here is "i";    a property

values.reverse()                # returns None; means doesn't return anything
print(values)
print(values[0])
print(values[-1])

values2 = array(values.typecode, (a*a for a in values))

for i in range(len(values)):    # old array
    print(values[i])

for i in values2:               # new array
    print(i)

seq = array('w', ['a','e','i'])
print(seq)

i=0
while i<len(values2):
    print(values2[i])
    # i++                     # SyntaxError: invalid syntax
    i+=1


# TAKING ARRAY ELEMENTS AS USER INPUT
from array import *

arr = array('i', [])        # creating an (signed integer) empty value

n = int(input("Enter length of array: "))
for i in range(n):
    x = int(input("Enter array elements: "))
    arr.append(x)

print(arr)

item = int(input("Enter item to be searched in arr: "))
index=0
for ele in arr:
    if ele==item:
        print(index)
        break
    index+=1

print(arr.index(item))          # index of 1st occurance of item in arr



###################################################
# CREATING ARRAYS IN PYTHON WITH NUMPY
###################################################

# 1) array()

from numpy import *

arr1 = array([2,3,5,6])
print(arr1)                             # [2 3 5 6]
print(arr1.dtype)                       # int64

arr2 = array([2,3,5,6,5.9])             # IMPLICIT CONVERSION
print(arr2)                             # [2. 3. 5. 6. 5.9]
print(arr2.dtype)                       # float64

arr3 = array([2,4,7,8.9], int)
print(arr3)                             # [2 4 7 8]
print(arr3.dtype)                       # int64

arr4 = array([2,4,7.9,8], float)
print(arr4)                             # [2.  4.  7.9 8. ]
print(arr4.dtype)                       # float64


# 2) linspace()

from numpy import *

arr1 = linspace(0,15,16)    # (start,end,no. of division/parts to be done between start and end-both inclusive)
print(arr1)                                 # [ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12. 13. 14. 15.]
# it's float because we are dividing [0,15] in 16 parts and when comes to parts, it may usually take float.

arr2 = linspace(0,15)            # by default parts=20
print(arr2)                                 # [ 0.          0.30612245  0.6122449   0.91836735  1.2244898   1.53061224
 #  1.83673469  2.14285714  2.44897959  2.75510204  3.06122449  3.36734694
 #  3.67346939  3.97959184  4.28571429  4.59183673  4.89795918  5.20408163
 #  5.51020408  5.81632653  6.12244898  6.42857143  6.73469388  7.04081633
 #  7.34693878  7.65306122  7.95918367  8.26530612  8.57142857  8.87755102
 #  9.18367347  9.48979592  9.79591837 10.10204082 10.40816327 10.71428571
 # 11.02040816 11.32653061 11.63265306 11.93877551 12.24489796 12.55102041
 # 12.85714286 13.16326531 13.46938776 13.7755102  14.08163265 14.3877551
 # 14.69387755 15.        ]


# 3) arange()

from numpy import *

arr1 = arange(1,15,2)               # (start,end,step) just like range(); here it's [1,15) - 15 exclusive just like range()
print(arr1)                         # [ 1  3  5  7  9 11 13]


# 4) logspace()

import numpy

arr1 = numpy.logspace(1,40,5)       # (start,end,no_of_parts_between_start_and_end) - but here, parts are logarithm based
print(arr1)                         # [1.00000000e+01 5.62341325e+10 3.16227766e+20 1.77827941e+30 1.00000000e+40]
print(arr1[0])                      # 10.0
print('%.2f' %arr1[0])              # 10.00
print(arr1[4])                      # 1e+40
print('%.2f' %arr1[4])              # 10000000000000000303786028427003666890752.00
# the difference between linspace() and logspace() is that linspace has normal values in parts but in logspace, parts are log value based - logarithmic spacing
# numpy.logspace(start, stop, num)
# This function returns **num numbers spaced evenly on a logarithmic scale (not a linear one), between 10^start and 10^stop.
# start: exponent of base 10 at the beginning
# stop: exponent of base 10 at the end
# num: how many values to generate (default is 50)
# 📌 So in your case:
# arr1 = numpy.logspace(1, 40, 5)
# means:
# Generate 5 numbers between 10¹ (10) and 10⁴⁰ (1e+40) — spaced logarithmically.

# 🧮 Is numpy.logspace() log-based?
# Yes — it is logarithmic in spacing, but not because it calculates logarithms, rather because it uses exponential steps that are evenly spaced on a log scale.
#
# 🤓 What's happening in logspace(start, stop, num)?
# Let’s take this:
# np.logspace(1, 40, 5)
# This gives you:
# [10^1, 10^10.75, 10^20.5, 10^30.25, 10^40]
# So it is:
# Picking evenly spaced numbers between 1 and 40 → [1.0, 10.75, 20.5, 30.25, 40.0]
# Then calculating 10 raised to each of those numbers → [10^1, 10^10.75, ..., 10^40]
#
# 📊 Why is this called "log" space?
# Because if you take the log₁₀ of the result, the values fall on a linear scale.
#
# In other words:
# The output values themselves are exponential (very large numbers)
# But the spacing of their exponents is linear → which makes the scale logarithmic
# That’s what a logarithmic scale is.
#
# 🔄 In short:
# Feature	np.logspace(...)
# Is it based on logs?	✅ Yes — spacing is logarithmic
# Does it take log()?	❌ No — it raises base to a power
# What’s returned?	Numbers like 10^x, not log(x)


# 5) zeros() and ones()

import numpy

arr1 = numpy.ones(5)        # creates an array of 5 values with 1 as its elements
arr2 = numpy.zeros(5)       # creates an array of 5 values with 0 as its elements
print(arr1)                 # [1. 1. 1. 1. 1.]
print(arr2)                 # [0. 0. 0. 0. 0.]


#################################
# VECTORIZED OPERATIONS,
# COPYING AN ARRAY IN PYTHON
#################################

from numpy import *

arr1 = array([1,2,3,4,5])
arr2 = array([5,6,7,8,9,10])
arr3 = array([5,6,7,8,9])

print(arr1 +10)                 # [11 12 13 14 15]
print(arr2 *2)                  # [10 12 14 16 18 20]

# arr3 = arr1 + arr2;
# print(arr3)                   # ValueError: operands could not be broadcast together with shapes (5,) (6,)

arr4 = arr1 + arr3;
print(arr4)                     # [ 6  8 10 12 14]

print(sin(arr1))                # [ 0.84147098  0.90929743  0.14112001 -0.7568025  -0.95892427]
print(cos(arr1))                # [ 0.54030231 -0.41614684 -0.9899925  -0.65364362  0.28366219]
print(log(arr1))                # [0.         0.69314718 1.09861229 1.38629436 1.60943791]
print(sqrt(arr1))               # [1.         1.41421356 1.73205081 2.         2.23606798]
print(sum(arr1))                # 15
print(max(arr1))                # 5
print(min(arr1))                # 1
print(sort(arr1))               # [1 2 3 4 5]
print(concatenate([arr1,arr2])) # [ 1  2  3  4  5  5  6  7  8  9 10]


# SHALLOW COPY - change in original array, will reflect in copied array; since there is single array being referenced by both variables
arr4 = arr2                     # same array is being referenced by both arr2 and arr4 variables
print(arr2)                     # [ 5  6  7  8  9 10]
print(arr4)                     # [ 5  6  7  8  9 10]
print(id(arr2))                 # 2333782868976
print(id(arr4))                 # 2333782868976
arr2[0] = 50
print(arr2)                     # [50  6  7  8  9 10]
print(arr4)                     # [50  6  7  8  9 10]

arr5 = arr2.view()              # a new array with different address gets created and being referenced by arr5
print(arr2)                     # [50  6  7  8  9 10]
print(arr5)                     # [50  6  7  8  9 10]
print(id(arr2))                 # 2333782868976
print(id(arr5))                 # 1284820136848
arr2[1] = 60
print(arr2)                     # [50 60  7  8  9 10]
print(arr4)                     # [50 60  7  8  9 10]

# DEEP COPY - change in original array, will not reflect in copied array; since these are two different array
arr6 = arr2.copy()
print(arr2)                     # [50 60  7  8  9 10]
print(arr6)                     # [50 60  7  8  9 10]
print(id(arr2))                 # 2333782868976
print(id(arr6))                 # 2821468702640
arr2[2] = 77
print(arr2)                     # [50 60 77  8  9 10]
print(arr6)                     # [50 60  7  8  9 10]



#################################################
# CREATING MULTI-DIMENSIONAL ARRAY (EX. MATRIX)
#################################################

from numpy import *

arr1 = array([
                [1,2,3,99,55,34],
                [4,5,6,10,20,10]
             ])
print(arr1)                 # [[1 2 3]
                            #  [4 5 6]]
print(arr1.dtype)           # int64 --> data-type - what kind of values, this array holds
print(arr1.ndim)            # 2 --> no. of dimensions - which dimensional array
print(arr1.shape)           # (2, 3) --> tuple of no. of rows and no. of columns
print(arr1.size)            # 6 --> size of (no. of elements in) entire array

arr2 = arr1.flatten()       # flattens the 2D array to 1D array
print(arr2)                 # [1 2 3 4 5 6]

arr3 = arr1.reshape(3,4)    # reshape the array with 3 rows and 4 columns
print(arr3)
# [[ 1  2  3 99]
#  [55 34  4  5]
#  [ 6 10 20 10]]

arr4 = arr1.reshape(2,2,3)  # reshape the array with 2 arrays with 2 rows and 3 columns each; 2*2*3=12elements
print(arr4)
# [[[ 1  2  3]
#   [99 55 34]]
#
#  [[ 4  5  6]
#   [10 20 10]]]
#### one big array, which has 2 two-dim array which has 2 single-dim array ehich has 3 values.
'''

from numpy import *

arr5 = array([
                [1,2,3],
                [4,5,6]
             ])
print(arr5)
# [[1 2 3]
#  [4 5 6]]

# MATRIX CREATION AND MANIPULATION
mat = matrix(arr5)
mat1 = matrix('10 20 30 ; 40 50 60 ; 70 80 90')
mat2 = matrix("1,3,5 ; 5,7,9; 5,6,7")
print(mat)
# [[1 2 3]
#  [4 5 6]]
print(mat1)
# [[10 20 30]
#  [40 50 60]
#  [70 80 90]]
print(mat2)
# [[1 3 5]
#  [5 7 9]
#  [5 6 7]]

print(diagonal(mat2))           # [1 7 7]
print(mat2.max())               # 9

mat3 = mat1 + mat2;
print(mat3)
# [[11 23 35]
#  [45 57 69]
#  [75 86 97]]

mat4 = mat1*mat2;
print(mat4)
# [[ 260  350  440]
#  [ 590  830 1070]
#  [ 920 1310 1700]]


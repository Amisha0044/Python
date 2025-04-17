###########################################
# IMPORTING MODULE
###########################################
'''
from calculator_module import *

summ = add(5,6)
print(summ)


import calculator_module

sub = calculator_module.sub(7,9)
print(sub)
'''


###########################################
# SPECIAL VARIABLE: __name__
###########################################

print(__name__)             # __main__

import calculator_module    # Hello,  calculator_module
print("bye, ", __name__)    # bye,  __main__
print("only 3 print statements in this file.. ends here..")

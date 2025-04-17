#########################################
# OOPS PILLARS:
#
# 1) Encapsulation
# 2) INHERITANCE
# 3) POLYMORPHISM
# 4) ABSTRACTION
##########################################


###########################################
# INHERITANCE
###########################################
'''
# SINGLE LEVEL INHERITANCE (A -> B)

# A - super class/parent class
class A:
    def feature1(self):
        print("feature-1 working..")
    def feature2(self):
        print("feature-2 working..")

# b - sub-class/child class
class B(A):     # class B is inhering all the features/properties from class A
    def feature3(self):
        print("feature-3 working..")
    def feature4(self):
        print("feature-4 working..")

a1 = A()        # A() is the constructor
a1.feature1()
a1.feature2()

b1 = B()
b1.feature3()
b1.feature4()
b1.feature1()
b1.feature2()


# MULTI LEVEL INHERITANCE (A -> B -> C)

# A - super class/parent class
class A:
    def feature1(self):
        print("feature-1 working..")
    def feature2(self):
        print("feature-2 working..")

# B - sub-class/child class
class B(A):     # class B is inhering all the features/properties from class A
    def feature3(self):
        print("feature-3 working..")
    def feature4(self):
        print("feature-4 working..")

# C - sub-class/child class
class C(B):     # class C is inhering all the features/properties from class B
    def feature5(self):
        print("feature-5 working..")

a1 = A()        # A() is the constructor
a1.feature1()
a1.feature2()

b1 = B()
b1.feature3()
b1.feature4()
b1.feature1()
b1.feature2()

c1 = C()
c1.feature1()
b1.feature2()
c1.feature3()
b1.feature4()
c1.feature5()


# MULTIPLE LEVEL INHERITANCE (A,B -> C)

# A - super class/parent class
class A:
    def feature1(self):
        print("feature-1 working..")
    def feature2(self):
        print("feature-2 working..")

# B - super/parent class
class B:
    def feature3(self):
        print("feature-3 working..")
    def feature4(self):
        print("feature-4 working..")

# C - sub-class/child class
class C(A,B):     # class C is inhering all the features/properties from class A and B both
    def feature5(self):
        print("feature-5 working..")

a1 = A()        # A() is the constructor
a1.feature1()
a1.feature2()

b1 = B()
b1.feature3()
b1.feature4()

c1 = C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()
'''



#########################################
# CONSTRUCTOR IN INHERITANCE:
# - How Constructor behaves in Inheritance?
# - How to use super() in Inheritance?
# - MRO (Method Resolution Order)
#########################################
'''
# A - super class/parent class
class A:
    # by default, every class has (an empty) constructor i.e. __init__() even if you don't define it explicitely.
    def __init__(self):
        print("in A init")
    def feature1(self):
        print("feature-1 working..")
    def feature2(self):
        print("feature-2 working..")

# b - sub-class/child class
class B(A):     # class B is inhering all the features/properties from class A
    def feature3(self):
        print("feature-3 working..")
    def feature4(self):
        print("feature-4 working..")

class C(A):
    def __init__(self):
        print("in C init")  # by default, when object of child class is created, it calls it's own constructor.

class D(A):
    def __init__(self):
        super().__init__()  # using super() method, we can access the properties of parent class
        print("in D init")

a1 = A()        # A() is the constructor, constructor of A is called automatically hen creating object of class A
a1.feature1()   # in A init ;   feature-1 working..

b1 = B()        # in A init
b1.feature1()   # feature-1 working..

c1 = C()        # in C init
c1.feature1()   # feature-1 working..

d1 = D()        # in A init ;   in D init
d1.feature1()   # feature-1 working..



class A:
    def __init__(self):
        print("in A init")
    def feature1(self):
        print("feature 1-A working..")

class B:
    def __init__(self):
        print("in B init")
    def feature1(self):
        print("feature 1-B working..")
    def feature2(self):
        print("feature 2 working..")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("in C init")
    def feat(self):
        super().feature2()

c1 = C()    # in A init ;   in C init

# MRO (Method Resolution Order):
# - whenever you have multiple inheritance, it goes from left to
# - hence, when called super().__init__(self), constructor of A was
# - same goes with the methods as well.

c1.feature1()   # feature 1-A working..

c1.feat()       # feature 2 working..




################################################################
# POLYMORPHISM
# - Poly (many) + Morphism (form) = one thing can take multiple forms
# - Ex. as humans, we have different forms. As the situation changes, we change ourselves i.e. we behave differently at different places like office, home, with friends etc. So humans are polymorphic.
# - Similarly, objects can have multiple forms.
# - We use this concept when we want to achieve: Loose coupling, Dependency injection, Interface
# - 4 ways of implementing the polymorphism:
#     * Duck typing
#     * Operator overloading
#     * Method overloading
#     * Method overriding
################################################################

# DUCK TYPING
# Duck Test (a Saying): If it (a bird) looks like a duck, swims like a duck, and quacks like a duck, then it's probably a duck.
# i.e. if behaviour of bird is matching with duck, then it's a duck.

# Python is dynamically types language meaning, memory for the variables (just a name to the memory) is allocated at the run-time.

class PyCharm:
    def execute(self):
        print("compiling")
        print("running")

class VSCode:
    def execute(self):
        print("spell check")
        print("GitHub copilot use")
        print("compiling")
        print("running")

class Laptop:
    def code(self, ide):
        ide.execute()

ide1 = PyCharm()
ide2 = VSCode()
lap = Laptop()

lap.code(ide1)           # compiling ;   running
lap.code(ide2)           # spell check  ;   GitHub copilot use  ;   compiling   ;   running

# behaviour changes based on the ide object being passed to lap.code()
# Just like a duck test, if there is an ide and has execute() method, that's it, we are not concerned about which class's object it is, but we are only concerned about it has the method execute() and that's duck typing.



################################################################
# OPERATOR OVERLOADING in PYTHON
# __add__(), __sub__() etc --> called MAGIC METHODS
################################################################

a = 5
b = "world"
c = 6
d = "hello"
# print(a+b)            # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(a+c)              # 11
print(int.__add__(a,c)) # 11
print(d+b)              # helloworld
print(str.__add__(d,b)) # helloworld

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        res1_int = self.m1 + other.m1
        res2_int = self.m2 + other.m2
        s3 = Student(res1_int,res2_int)
        return s3

    def __gt__(self, other):
        stud1_res_int = self.m1 + self.m2
        stud2_res_int = other.m1 + other.m2
        if stud1_res_int > stud2_res_int:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)

s1 = Student(90,100)
s2 = Student(80,90)

s3 = s1 + s2
s4 = Student.__add__(s1,s2)
print(s3.m1)            # 170
print(s4.m1)            # 170
print(s3.m2)            # 190
print(s4.m2)            # 190

if s1>s2:
    print("s1:student-1 wins")
else:
    print("s2:student-2 wins")

print(a)                # 5
print(a.__str__())      # 5 --   behind the scenes
# print(s1)               # <__main__.Student object at 0x0000018A94E86A50> - giving the address of s1 and not value   --  before overriding __str__() method
# print(s1.__str__())     # <__main__.Student object at 0x0000018A94E86A50> - means it's also calling .__str__()   --  before overriding __str__() method
print(s1)               # 90 100    --  after overriding __str__() method
print(s1.__str__())     # 90 100    --  after overriding __str__() method
'''


###################################################################
# METHOD OVERLOADING & METHOD OVERRIDING:
#
# - operator overloading -- operator (+,-,*,/,%) will remain same but type of operands/parameters will change
# - Ex. __add__() takes different types of args
#
# - types of polymorphism:
#   * method overloading (not supported in Python - two methods in a class with same name but with different signature),
#   * method overriding (supported in Python - two methods with same name and same signature in child and parent class)
###################################################################

# METHOD OVERLOADING (not supported in Python)
'''
class method_overloading_indirectly:
    def sum(self, a=None, b=None, c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        elif a!= None:
            s = a
        else:
            s = 0
        return s

obj1 = method_overloading_indirectly()

print(obj1.sum())
print(obj1.sum(3))
print(obj1.sum(2,55))
print(obj1.sum(2,5,7))


# METHOD OVERRIDING (supported))

class A:
    def show(self):
        print("in A show")

class B(A):
    def show(self):         # method overriding
        print("in B show")

b1 = B()
b1.show()                   # in B show -- child class method will be called as each function gives priority to its own preperties first. TO explicitely call parent class method, use super()
'''


###################################################################
# ABSTRACT CLASS & ABSTRACT METHOD in PYTHON
#
# - Python by default doesn't support abstract classes.
# - But we have abc (Abstract Base Classes) module to achieve abstract classes.
#
# - What is abstract class? --
#   * abstract class is a class which has at least one abstract method
#   * abstract methods are methods which don't have any definition/body'
#   * you can't create object of abstract class
#
# - Why to use abstract class? --
#   * when you don't want to implement functionality in beginning, and also want to achieve loose-coupling.
###################################################################

# declaration = no body
# definition = declaration + body

from abc import ABC,abstractmethod

class Computer(ABC):        # now, an abstract class
    @abstractmethod         # decorator to make a method an abstract method
    def process(self):
        pass

# if you don't define/implement all the abstract method of parent class, then you can't instantiate it as this class will also become an abstract class
class Laptop(Computer):
    pass

class Mobile(Computer):
    def process(self):
        print("running")

class Techie:
    def work(self, com):        # techie also needs a machine (can be laptop, desktop, mobile, anything) to work with
        print("solving problems")
        com.process()

# c1 = Computer()             # TypeError: Can't instantiate abstract class Computer without an implementation for abstract method 'process'
# c1.process()

# l1 = Laptop()               # TypeError: Can't instantiate abstract class Laptop without an implementation for abstract method 'process'
# l1.process()

m1 = Mobile()
m1.process()                # running

tec1 = Techie()
# tec1.work()                 # solving problems
tec1.work(m1)               # solving problems  ;   running


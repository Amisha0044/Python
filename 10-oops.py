##########################################
# CLASS & OBJECTS
##########################################
'''
class Computer:
    # define attributes (variables) and behavior (methods)
    def config(self):           # 'self' is the object we will be passing when calling this method.
        print("15, 16gb, 1TB")

# creating object of class Computer
comp1 = Computer()
print(type(comp1))           # <class '__main__.Computer'>
# module name is __main__ as we are running the code from this same file, and then followed by class name COmputer

# <class 'str'>   --  inbuilt class
# <class '__main__.Computer'>  --  user-defined class


# in order to access methods of class, we can access it using className.
# config()                  # NameError: name 'config' is not defined
# Computer.config()         # TypeError: Computer.config() missing 1 required positional argument: 'self'
# this is because config() method will change its behaviour based on the object, since every object has difference behaviour based on their attributes (what they know).
Computer.config(comp1)      # 15, 16gb, 1TB


comp2 = Computer()
Computer.config(comp2)      # 15, 16gb, 1TB


# we can also access the class methods directly using object name.
comp1.config()              # 15, 16gb, 1TB
comp2.config()              # 15, 16gb, 1TB
# behind the scenes, config() will take comp1 as an argument and will pass it to 'self'.

# Ex.
a=5
print(a.bit_length())       # 3
# here also, if you press cntr and click on bit_length(), you'll see, this method also expect an object as its arg since self is passsed there. But here, we're not passing any object beacause 'a' is being passed as its arg in the backend.



###################################################
# SPECIAL METHOD: __init__(self)
###################################################

class Computers:
    def __init__(self, cpu, ram):     # to initialize class variables, will be called automatically whenever the object of the class is created
        print("in init")
        self.cpu = cpu                # assigning value of cpu variable to the object 'self' variable
        self.ram = ram

    def config(self):
        print("Config is: ", self.cpu, self.ram)

com1 = Computers('i5',16)   # passing 3 args in backend: com1, 'i5' and 16
com2 = Computers('Ryzen 3', 8)

com1.config()
com2.config()



###############################################
# CONSTRUCTOR AND SELF
###############################################

class Computer:
    def __init__(self):
        self.name = "Navin"
        self.age = 33

    def update_age(self):
        self.age = 25

    def compare(self, other):
        if self.age==other.age:
            return True
        else:
            return False

comp1 = Computer()
comp2 = Computer()

print(id(comp1))            # 2249322424576
print(id(comp2))            # 2249325103376

print(comp1.name)           # Navin
print(comp1.name)           # Navin

comp1.name = "Rashi"
comp1.age = 21
print(comp1.name)           # Rashi
print(comp2.name)           # Navin

comp1.update_age()
print(comp1.age)           # 25
print(comp2.age)           # 33

if comp1.compare(comp2):    # self = comp1, other = comp2
    print("they are same")
else:
    print("they are different") # they are different



###############################################
# TYPES OF VARIABLES in OOPS
# 1) Instance Variable
#    - different value for different object
#    - vary with object; change in value for one object won't affect the value for other objects
#    - defined inside __init__()
# 2) Class (Static) Variable
#    - value remains same for all objects
#    - change in this variable, will reflect for all objects
#    - defined outside of __init()
###############################################

class Car:
    wheels = 4              # wheels = class(static) variable - belongs to Class namespace
    def __init__(self):
        self.mil = 60       # mil = instance variables - belong to Instance namespace
        self.comp = "BMW"   # comp = instance variables - belong to Instance namespace

c1 = Car()
c2 = Car()

c2.mil=100
print(c1.comp, c1.mil, c1.wheels)
print(c2.comp, c2.mil, c2.wheels)

# static variables can be accessed either via className or objectName
Car.wheels = 5
print(c1.comp, c1.mil, c1.wheels)
print(c2.comp, c2.mil, c2.wheels)

# NAMESPACE:
# - namespace is an area where you create and store object/variable
# - types of namespaces:
#   1) Class namespace - here you store all the class variables
#   2) Object/Instance namespace - here you store all the instance variables



########################################################
# TYPES OF METHODS IN PYTHON
# 1) Instance method
     - Accessor methods (getters - to fetch the value of instance variables),
     - Mutator methods (setters - to modify the value of instance variables)
# 2) Class method
# 3) Static method
########################################################

class Student:

    school = "Telusko"              # static/class variable

    def __init__(self,m1,m2,m3):    # m1,m2,m3 - instance variable
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):                  # instance method (works on the object) - self is passed, means it belongs to specific object
        return (self.m1+self.m2+self.m3)/3
    def get_m1(self):
        return self.m1
    def set_m1(self, val1):
        self.m1 = val1

    @classmethod                    # to make a method as class method, use @classmethod decorator
    def get_school(cls):            # class method (works on class variable) - 'cls' should be passed as an arg in class method
        return cls.school

    @staticmethod                   #  to make a method as static method (the method which has nothing to do with class variables and instance variables), use @staticmethod decorator
    def info():                     # neither self not cls, nothing - static method
        print("this is Student class")
    # this method has nothing to do with instance variables and class variables.
    # when you want to perform some operation which has something to do with other class' object; or some operations like factorial, fibonacci etc. which has nothing to do with the class variables or instance variables.

s1 = Student(44,78,56)
s2 = Student(33,90,77)
print(s1.avg())                     # 59.333333333333336
print(s2.avg())                     # 66.66666666666667
print(Student.get_school())         # Telusko
Student.info()                      # this is Student class
s1.get_school()                     # (no output - blank)
s1.info()                           # this is Student class



######################################################
# INNER CLASS
# - Class inside a class, is called inner class
# - We use inner class when we know that this inner class will only be use in outer class and nowhere else.
######################################################

class Student:                      # OUTER CLASS
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.lap = self.Laptop()    # creating object of Laptop class and assigning it to self.lap (object name)
    def show(self):
        print(self.name, self.roll)
        self.lap.show()

    class Laptop:                   # INNER CLASS
        def __init__(self):
            self.brand = "HP"
            self.cpu = 'i5'
            self.ram = 8
        def show(self):
            print(self.brand, self.cpu, self.ram)

    class Mobile:                   # INNER CLASS
        def __init__(self):
            self.brand = "Motorola"
            self.price = 25000

s1 = Student('Ayushi', 8)
s2 = Student("Amisha", 1)

# print(s1.name, s1.roll)                 # Ayushi 8
s1.show()                               # Ayushi 8; HP i5 8

print(s1.lap.brand)                     # HP    -   s1.lap because lap object is inside Student Class
# OR
lap1 = s1.lap                           # creating an object of inner class
lap2 = s2.lap
print(id(lap1))                         # 2696961223248
print(id(lap2))                         # 2696983180176

mob1 = Student.Mobile()                 # creating an object of inner class, outside the outer class
# Student.Mobile() because Mobile class belongs to Student class

# We can create object of inner class inside the outer class.
# OR we can create object of inner class outside the outer class, provided we use class name to call it.
'''




# if running this file, __name__ hold __main__ value, and prints Hello, __main__
# but if importing this file as module into another file and running that file, __name__ will hold "theModuleName", and it will print Hello, moduleName
def display():
    print("Hello, ", __name__)      # Hello,  __main__

def welcome_main():
    print("Hello, Welcome user!")
    print("please feel comfortable to explore our calculator products..")

# execute display() in both the case: if this file is being executed as the first file or if this file is imported into another file and the other file is being executed.
display()

# execute welcome_main() function only if this file is the main file to be executed or if this is the file which is getting executed directly.
# and if this file/module is not the frst file i.e. being imported by other file, then don't execute welcome_main()
if __name__=="__main__":
    welcome_main()

def add(a,b):
    return a+b

def sub(a,b):
    return a-b;

def mul(a,b):
    return a*b

def div(a,b):
    return a/b;



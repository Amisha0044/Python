##########################################
# MULTI THREADING
#
# THREAD:
# - thread is a sub-process; a big task is divided into smaller parts, each smaller part is called thread.
# - ex. MS word(a process) has multiple features/sub-processes like font change, export, save file, create file(thread) etc.
# - One single task has multiple processes, further each process is broken down into multiple sub-processes. These sub-processes are threads.
# - a light-weight process
#
# - multi-tasking: in modern days' computers, we have multicore cpu, also OS are able to do multi-tasking means can run multiple applications at once like MS word, music, chrome, vscode etc.
# - every application(task) has multiple threads.
# - you can't run multiple task at the same time in OS; so cpu do time sharing means every task gets some time.
#
# - threads get executed on different cpu cores.
# - cpu allots the time to each thread to execute.
# - advantage of using multiple threads is that we can use all our cpu cores.
#
##########################################
'''
from threading import *
from time import sleep

class Hello(Thread):    # making the class a thread, by extending this class to Thread class
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

hel = Hello()
hi = Hi()

# hel.run()
# hi.run()
# by default each execution has 1 thread. So, even if you don't create any thread, there's a thread called Main thread.
# so, by default, we have a Main thread executes all the statements.

# both the above functions got executed one by one.
# what if we want to execute both the functions parallely at the same time in different cores or even in the same core???? - create 2 different threads
hel.start()     # to execute thread hel; it automatically calls the run() method
sleep(0.2)
hi.start()      # to execute thread hel
# now both threads hel and hi are getting executed parallely but not the way we want like hello hi hello hi etc.

# schedulers give time to execute each thread.
# and our systems are too fast that during execution of 1 thread, it's able to print hello 8-10 times and same for hi.
# so, we will use sleep(sec) to make it sleep/wait.
# yes and it worked.
# but it printed hellohi and hihello as well; which is called "COLLISION" because after sleep and waking up, both threads are getting to cpu at the same time and are getting printed.
# so, to avoid this collision situation, we can use sleep() of 0.2 sec in between starting both threads.

hel.join()      # asking Main thread to wait for hel thread to complete (and join/come back)
hi.join()       # asking Main thread to complete (since Main is the thread which is responsible to execute all the statements)

print("Bye")
# so now, there were total 3 threads running: Main, hel and hi
# hence, we got hello hi hellobye hi... because main was also parallely getting executed.
# if we want to print bye at the end, we can ask Main thread to wait for hel and hi threads to complete and join back using join().
'''
from os import write

###########################################
# FILE HANDLING
#
# File:
# - data stored in variables is temporary (once you close the application, variable data will be lost), but what if you want to store data for future use?
# - for this permanent storage, we can use ex mysql db but that will store data in table form and is very complex, but what if we have text data.
# - in such cases, we can use files.
#
# Python provides some in-build functions to work with files.
# Ex. open(), read(), write(), close(); Modes of opening a file: r, w, a
#
###########################################
'''
# f = open("file1",'r')   # f - object/reference - basically holds "file1" ; -- opening the file named file1 in read mode
# # print(f)                # <_io.TextIOWrapper name='file1' mode='r' encoding='cp1252'>
# # print(f.read())         # to read data from file; --    hello ;   thanks for checking the file    ;   bye bye
# # print(f.readline())     # to read 1st line and moves to pointer to the next line; --  hello
# # print(f.readline())     # thanks for checking the file;  -- getting extra blank line since readline() gives new line and print() also
# # print(f.readline(3))    # reads first 3 characters from the line
# # print(f.readlines())    # returns a list of all the lines   --  ['hello\n', 'thanks for checking the file\n', 'bye bye\n']
#
# # f1 = open('file2','w')
# # f1.write("test..")
# # f1.write("checking..\n")
# # f1.write("hello\nthanks for writing into this file\nhave a great day ahead\nthanks")
# # f1.write("hello\nthanks for writing into this file\nhave a great day ahead\nthanks")    # it re-writes the file and doesn't append
#
# # f2 = open('file1','a')
# # f2.write("testing completed")     # appends this text at the end of file1
#
# f3 = open('file3-copyFromFile1','w')
#
# # copying the data from file1 to file3 as it is
# for data in f:
#     print(data)         # printing data of file1 with extra blank line after each line due to print()
#     f3.write(data)


# how to read an image file?

# f4 = open('ganesh-4419043_1280.jpg','r')
# for data in f4:
#     print(data)         # UnicodeDecodeError: 'charmap' codec can't decode byte 0x8d in position 261: character maps to <undefined>

# in files, we have two different modes: text mode and binary mode
# for a file having characters, numbers, you can use text mode
# but for an image file, we don't have characters inside image, but we have binary format. Hence, we should use binary mode

f4 = open('ganesh-4419043_1280.jpg','rb')   # read binary
f5 = open('Ganeshji-pic.jpg','wb')
for data in f4:
    print(data)
    f5.write(data)

f5.close()
f4.close()
'''




###################################################
# COMMENTS IN PYTHON
#
# what is comment:
# - a statement or set of statements that is ignored by compiler and interpreters and will never be executed.
#
# why to use comments:
# - to make it easy for yourself and others to understand what this code is doing.
#
# type of comments:
# 1) single line comments -- #
# 2) multi line comments -- ''' ''' or """ """ (not recommended to use multi-line comments)
#
# why not to use multi line comments using ''' ?
# - because ''' are used for special purpose i.e. for documentation, hence parser won't ignore it
# - so, always try to use # even for comments in multiple lines.
#
###################################################

print("hello")

# single line comment

'''
multi
line
comment
'''

"""
but 
multi line comment
is not recommended to use this way using ''' or \"\"\""""

print("bye")





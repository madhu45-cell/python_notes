#Open a File on the Server
'''
To open the file, use the built-in open() function.
The open() function returns a file object, which has a read() method for reading the content of the file:
'''
f = open("demofile.txt", "r")
print(f.read())
# output
# Hello! Welcome to demofile.txt
# This file is for testing purposes.
# Good Luck!

# Read Only Parts of the File
'''By default the read() method returns the whole text, but you can also specify how many characters you want to return:
file.read(no of char) / file.read()
'''
f = open("demofile.txt", "r")
print(f.read(5))
# output
# Hello

# Read Lines
'''You can return one line by using the readline() method:'''
f = open("demofile.txt", "r")
print(f.readline())
# output
# Hello! Welcome to demofile.txt
'''you can also return all lines in List by using the readlines(), where lines are elements of List'''
f = open("demofile.txt", "r")
print(f.readlines())
# output
# ['Hello! Welcome to demofile.txt\n', 'This file is for testing purposes.\n', 'Good Luck!']



# Close Files
'''It is a good practice to always close the file when you are done with it.'''
f = open("demofile.txt", "r")
print(f.readline())
f.close()
'''You should always close your files. In some cases, due to buffering, changes made to a file may not show until you close the file.'''




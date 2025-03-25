# Write to an Existing File
'''To write to an existing file, you must add a parameter to the open() function:
"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content
'''

'''Open the file "demofile2.txt" and append content to the file:
if file not exist they will make it. and add the line
'''
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()
#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())



'''Open the file "demofile2.txt" and overwrite the content:
and overwrite the existens content.
'''
f = open("demofile2.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
#open and read the file after the overwriting:
f = open("demofile2.txt", "r")
print(f.read())





# Delete a File
'''To delete a file, you must import the OS module, and run its os.remove() function:'''
import os
os.remove("demofile3.txt")


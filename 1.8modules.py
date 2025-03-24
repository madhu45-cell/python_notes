# Python Modules
# What is a Module?
'''
Consider a module to be the same as a code library.
A file containing a set of functions you want to include in your application.
'''

# Create a Module
'''To create a module just save the code you want in a file with the file extension .py:
'''
'''Save this code in a file named mymodule.py'''
def greeting(name):
  print("Hello, " + name)

# Use a Module
'''Now we can use the module we just created, by using the import statement:
When using a function from a module, use the syntax: module_name.function_name.
'''
'''Import the module named mymodule, and call the greeting function:'''
# import mymodule
# mymodule.greeting("Jonathan")


# Naming a Module
'''You can name the module file whatever you like, but it must have the file extension .py'''

# Re-naming a Module
'''You can create an alias when you import a module, by using the as keyword:'''
'''Create an alias for mymodule called mx:'''
# import mymodule as mx
# a = mx.person1["age"]
# print(a)


# Built-in Modules
'''There are several built-in modules in Python, which you can import whenever you like.'''
import platform
x = platform.system()
print(x) #Darwin


# Using the dir() Function
'''There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
The dir() function can be used on all modules, also the ones you create yourself.
'''
import platform
x = dir(platform)
print(x) #['AndroidVer', 'IOSVersionInfo', '_Processor', '_WIN32_CLIENT_RELEASES', '_WIN32_SERVER_RELEASES', '__builtins__', '__cached__', '__copyright__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_comparable_version', '_default_architecture', '_follow_symlinks', '_get_machine_win32', '_java_getprop', '_mac_ver_xml', '_node', '_norm_version', '_os_release_cache', '_os_release_candidates', '_parse_os_release', '_platform', '_platform_cache', '_sys_version', '_sys_version_cache', '_syscmd_file', '_syscmd_ver', '_uname_cache', '_unknown_as_blank', '_ver_stages', '_win32_ver', '_wmi', '_wmi_query', 'android_ver', 'architecture', 'collections', 'freedesktop_os_release', 'functools', 'ios_ver', 'itertools', 'java_ver', 'libc_ver', 'mac_ver', 'machine', 'node', 'os', 'platform', 'processor', 'python_branch', 'python_build', 'python_compiler', 'python_implementation', 'python_revision', 'python_version', 'python_version_tuple', 're', 'release', 'sys', 'system', 'system_alias', 'uname', 'uname_result', 'version', 'win32_edition', 'win32_is_iot', 'win32_ver']



# Import From Module
'''You can choose to import only parts from a module, by using the from keyword.'''
'''
Import only the person1 dictionary from the module:
'''
# from mymodule import person1
# print (person1["age"])




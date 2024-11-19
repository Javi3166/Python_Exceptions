# A python program can terminate immediately when it encounters an error. Errors can be either a syntax error or an exception.
print("\nA syntactical error happens when the program encounters an error with the syntax such as the following code"
      " in the comments:")
# a = 5print(a)
# or
"""
a = 5
print(a))
"""

print("\nIf the syntax is correct, but there is an error, it is known as an exception. There are several different error "
      "classes.")
print("\nFirst is the TypeError which is encountered when doing something like adding a number and a string.")
# a = 5 + '10'

print("\nThere is the ModuleNotFoundError when attempting to import a module that does not exist.")
# import somemodule


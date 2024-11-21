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

print("\nA NameError occurs when referencing a variable that is not defined.")
# a = 5
# b = c

print("\n A FileNotFoundError occurs when trying to find a file, but not able to.")
# f = open('somefile.txt')

print("\nA ValueError occurs when a function or operation receives an argument of the right type, but an inappropriate value.")
# a = [1, 2, 3]
# a.remove(4)

print("\nAn IndexError is when attempting to access an index that does not exist in a sequence.")
# a = [1, 2, 3]
# a[4]

print("\nA KeyError is when attempting to access a key that does not exist in a dictionary.")
# my_dict = {'name': 'Max'}
# my_dict['age']

print("\nIt is possible to force an exception to occur when a condition is met with the 'raise' keyword.")
x = 5
if x < 0:
      raise Exception('x should be positive')

print("\nIt is also possible to use 'assert' to force an exception with an AssertionError. "
      "The result will need to be False/Not True to trigger it.")
x = 5
assert (x >= 0), 'x should be positive'

print("\nIt is possible to catch exceptions with a try, except block and do specific tasks depending on the results.")
print("\nLeaving the except alone will catch any and all exceptions.")
try:
      a = 5 / 0
except:
      print("An error happened.")
print("\nIt's possible to have the specific error that occurred to be printed out..")
try:
      a = 5 / 0
except Exception as e:
      print(e)
print("\nIt is good practice to except only specific errors.")
try:
      a = 5 / 0
except ZeroDivisionError as e:
      print("There is an attempt to divide by zero.")
print("\nIt is possible to catch multiple different errors and have different outputs depending on the error.")
try:
      a = 5 / 1
      b = a + '10'
except ZeroDivisionError as e:
      print("There is an attempt to divide by zero.")
except TypeError as e:
      print("There is a mismatch of types affecting each other.")
print("\nIt is possible to use else statements if everything works out fine.")
try:
      a = 5 / 1
      b = a + 4
except ZeroDivisionError as e:
      print("There is an attempt to divide by zero.")
except TypeError as e:
      print("There is a mismatch of types affecting each other.")
else:
      print("Everything is fine.")
print("\nUsing the 'finally' keyword will have the code run no matter what whether an error occurred or not.")
try:
      a = 5 / 0
      b = a + 4
except ZeroDivisionError as e:
      print("There is an attempt to divide by zero.")
except TypeError as e:
      print("There is a mismatch of types affecting each other.")
else:
      print("Everything is fine.")
finally:
      print("Cleaning up...")

print("\nIt is possible to make custom errors by making it a subclass of the general Exception class.")
class ValueTooHighError(Exception):
      pass
def test_value(x):
      if x > 100:
            raise ValueTooHighError('The value is too high')
# test_value(200)

print("\nIt is possible to use the custom error in a try/except block.")
try:
      test_value(200)
except ValueTooHighError as e:
      print(e)

print("\nIt is possible to have the custom error class do more.")
class ValueTooLowError(Exception):
      def __init__(self, message, value):
            self.message = message
            self.value = value
def test_value(x):
      if x > 100:
            raise ValueTooHighError('The value is too high')
      if x < 5:
            raise ValueTooLowError('The value is too low', x)
try:
      test_value(1)
except ValueTooHighError as e:
      print(e)
except ValueTooLowError as e:
      print(e.message, "/ The value is:", e.value)
"""
Exercise 9: Recursion
---------------------

The Evil Wizard Malloc has attacked you and taken away your ability
to use loops!  The only way you can defeat him is by fighting back
using the power of recursion!

Below are function stubs for a variety of functions that are able
to be solved recursively.  For this exercise, you are not allowed
to use:

  * for loops
  * "while" loops
  * You may use list slicing, but you may not use the "reverse" slice
    (e.g, list[::-1])
  * Any built-in function that achieves the same result

You can use the included test_recursion.py script to test that your
functions work (and if you need hints for what the expected input/output 
should be).

"""

# Multiply all the elements in a list using recursion
def multiply_list(l):
    return 1

# Return the factorial of n
def factorial(n):
    return 1

# Count the number of elements in the list l without using loops or the len() function
def count_list(l):
    return 0

# Sum all of the elements in a list without using loops or the sum() function
def sum_list(l):
    return 0

# Reverse a list recursively without loops, the reverse() function or list[::-1]
def reverse(l):
    return []

# Fibonacci returns the nth fibonacci number. The nth fibonacci number is
# defined as fib(n) = fib(n-1) + fib(n-2)
def fibonacci(n):
    return 1

# Finds the item i in the list l.... RECURSIVELY
# Return the item if it is in the list or None if not found.
def find(l, i):
    return None

# Determines if a string is a palindrome
# A palindrome is any string that is the same forwards and backwords.
#   (e.g. radar, racecar, aibohphobia)
# Solve recursively, 
def palindrome(some_string):
    return False

# Given the width and height of a sheet of paper, and the number of times to fold it, return the final dimensions of the sheet as a tuple. Assume that you always fold in half along the longest edge of the sheet.
def fold_paper(width, height, folds):
    return (0, 0)

# Count up
# Print all the numbers from 0 to target.
# Use n to keep track of where you're at
# ex, to count from 1 - 100, call count_up(100, 1)
#
# Note: we don't have a test case for this one, so just run this
#       script directly
#
# Note #2: We're printing out the numbers, so this script does not 
#          need to return anything!
def count_up(target, n):
    pass

if __name__ == "__main__":
    count_up(100, 0)

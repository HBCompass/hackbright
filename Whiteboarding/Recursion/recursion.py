"""
Recursion

The Evil Wizard Malloc has attacked you and taken away your ability
to use loops! The only way you can defeat him is by fighting back
using the power of recursion!

Below are function stubs for a variety of functions that are able
to be solved recursively. For this exercise, you are not allowed
to use:

  * for loops

  * "while" loops

  * You may use list slicing, but you may not use the "reverse" slice
    (e.g, list[::-1])

  * Any built-in function that achieves the same result

If you run this script from the command line, it will execute the
built-in tests, and let you know which functions are either not
complete or not correct.

When all tests pass, this program will output:

    ** ALL TESTS PASS; GOOD WORK! **

"""


def multiply_list(lst):
    """Multiply all the elements in a list using recursion.
    
    
    >>> multiply_list([5, 2, 1, 4, 3, 6])
    720

    >>> multiply_list([5, 24, 48, 88])
    506880

    >>> multiply_list([5, 24, 48, 88, 0])
    0
    """

    if not lst:
        return 1

    return lst[0] * multiply_list(lst[1:])


def factorial(n):
    """Return the factorial of n.

    The factorial is the result of multiplying all integers from 1...n.

    >>> factorial(1)
    1

    >>> factorial(2)
    2

    >>> factorial(3)
    6

    >>> factorial(4)
    24
    """

    if n == 1:
        return 1

    return n * factorial(n - 1)


def count_list(lst):
    """Count the number of elements in the list without using loops or len().

    >>> count_list([5, 2, 1, 4, 3, 6])
    6

    >>> count_list([5, 24, 48, 88])
    4
    """

    if not lst:
        return 0

    return 1 + count_list(lst[1:])


def sum_list(lst):
    """Sum the items in the list without using loops or the sum() function.

    >>> sum_list([5, 2, 1, 4, 3, 6])
    21

    >>> sum_list([5, 24, 48, 88])
    165
    """

    if not lst:
        return 0

    return lst[0] + sum_list(lst[1:])


def reverse(lst):
    """Reverse a list recursively, without loops, reverse() function or list[::-1].

    >>> reverse([1, 2, 3, 4])
    [4, 3, 2, 1]

    >>> reverse([])
    []
    """

    if not lst:
        return []

    return [lst[-1]] + reverse(lst[0:-1])


def fibonacci(n):
    """Return the nth fibonacci number.

    The nth fibonacci number is defined as:

       fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)

    Use recursion to solve this.

    >>> fibonacci(1)
    1

    >>> fibonacci(2)
    1

    >>> fibonacci(3)
    2

    >>> fibonacci(4)
    3

    >>> fibonacci(5) 
    5

    >>> fibonacci(6)
    8

    >>> fibonacci(7)
    13

    >>> fibonacci(8)
    21

    >>> fibonacci(9)
    34
    """

    if n < 1:
        return 0
    
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def find(lst, i):
    """Find item i in the list lst.

    If the item is in the list, return it. Otherwise, return None.

    Use recursion to solve this.

    >>> find(["a", "b", "c"], "a")
    'a'

    >>> find(["a", "b", "c"], "c")
    'c'

    >>> find(["a", "b", "c"], "d")
    """

    if not lst:
        return None

    if lst[0] == i:
        return i

    return find(lst[1:], i)


def is_palindrome(some_string):
    """Is some_string a palindrome?

    A palindrome is any string that is the same forwards and backwords
    (e.g., "radar", "racecar", "aibohphobia")

    Solve this using recursion.

    >>> is_palindrome("a")
    True

    >>> is_palindrome("hello")
    False

    >>> is_palindrome("racecar")
    True

    >>> is_palindrome("foof")
    True

    >>> is_palindrome("foaf")
    False
    """

    if not some_string:
        return True

    if some_string[0] != some_string[-1]:
        return False

    return is_palindrome(some_string[1:-1])


def fold_paper(width, height, folds):
    """Find the dimensions of a folded piece of paper.

    Given a width and height of a piece of paper, and the number of times to fold it,
    return the final dimensions (as a tuple of width, height) of the paper. Assume that
    you always fold in half along the longest edge of the sheet (if they are the same
    length, fold along the width first.)

    >>> fold_paper(8.5, 11, 1)
    (8.5, 5.5)

    >>> fold_paper(8.5, 11, 2)
    (4.25, 5.5)

    >>> fold_paper(8.5, 11, 3)
    (4.25, 2.75)

    >>> fold_paper(8.5, 11, 4)
    (2.125, 2.75)

    >>> fold_paper(8.5, 11, 5)
    (2.125, 1.375)

    >>> fold_paper(10, 10, 2)
    (5.0, 5.0)

    >>> fold_paper(10, 10, 4)
    (2.5, 2.5)

    Let's make sure we handle the case of even sizes:

    >>> fold_paper(10, 10, 1)
    (5.0, 10.0)
    """

    if folds == 0:
        return float(width), float(height)

    if width >= height:
        return fold_paper(width / 2.0, height, folds - 1)

    else:
        return fold_paper(width, height / 2.0, folds - 1)


def count_up(n, target):
    """Print all integers from n to target, inclusive.
    
    >>> count_up(1, 5)
    1
    2
    3
    4
    5

    >>> count_up(0, 2)
    0
    1
    2

    >>> count_up(-1, 1)
    -1
    0
    1

    >>> count_up(0, 0)
    0

    >>> count_up(1, 0)
    """

    if n > target:
        return

    print n
    count_up(n + 1, target)


###########################################################################################

if __name__ == "__main__":
    from doctest import testmod
    print
    if testmod().failed == 0:
        print "    ** ALL TESTS PASS. GOOD WORK! **"
    print

List Operations
===============

### A few things about lists

First, work through the following resources on lists:

* http://learnpythonthehardway.org/book/ex32.html
* http://learnpythonthehardway.org/book/ex33.html
* http://learnpythonthehardway.org/book/ex34.html
* http://learnpythonthehardway.org/book/ex38.html
* http://learnpython.org/en/Lists
* http://docs.python.org/tutorial/introduction.html#lists
* http://docs.python.org/tutorial/datastructures.html#more-on-lists
        --> stop reading before section 5.1.1

### A few things about tests

#### Some background reading:

http://learnpythonthehardway.org/book/ex47.html

#### What's going on here?

In this exercise directory there are two files: `list_operations.py` and
`test_list_operations.py`.

`list_operations.py` contains lots of empty functions that take an input list and don't do anything.    
`test_list_operations.py` contains lots of full functions that ... ? Well, let's find out.

####Try it out!

Try running `python test_list_operations.py` at the CLI prompt. You should see a lot of console output that ends with the following text:
```
----------------------------------------------------------------------
Ran 25 tests in 0.007s

FAILED (failures=25)
```

Wow, 25 failures. That doesn't sound good. What just happened?


Well, `test_list_operations.py` just ran 25 'tests' on `list_operations.py` and none of them worked. How did it do that?

####What's a test?

Each function in `test_list_operations.py` (which I will now refer to as a test) does four things:    
1. Gets some sample data (initialized in `setUp()` and passed in to each function with `self` -- more on this on a later date)    
2. Sends the sample data through a `list_operations.py` function (there's one test function for each regular function)    
3. Defines what the correct output for each function should be based on the input    
4. Tests whether the result of the `list_operations.py` function matches the expected input ( it assertsEqual-ity )    

If all of the asserted equalness turns out true, then your test passes. If any of them fails, your test fails.    
All of your tests failed because, obviously, there's nothing in any of your `list_operation` functions. So whatever your function returns (it returns nothing) doesn't match what the test expects (very specific things, including not nothing).

For example: `test_1_A_head()` checks the function `head()` in `list_operations.py`. It asserts that the result of calling the function `head()` with the test data `months` should result in `'Jan'`.

One thing to note is that `test_1_A_head()` is laid out differently than a test like `test_1_J_replace_head()`. The latter calls the function first, then checks the result in a different step. **This is important!** Why?

When a test fails, it will print the un-matching-ness in the terminal. This may be helpful for troubleshooting your list operators. Also, sometimes you may see something like:
```
FAILED (failures=24, errors=1)
```
Don't get too excited that your failure number has gone down by one -- an error means that the function call errored out when the test called it. You'll be able to see the error message it returned if you scroll up in the terminal to that test's section.

### Go!

Your mission is to get all the tests to pass by actually writing the functions in `list_operations.py`. When you've succeeded, you'll see only this output when you run your tests: 
```
.........................
----------------------------------------------------------------------
Ran 25 tests in 0.002s

OK
```

[<img src="http://bit.ly/1pzkhYG">](http://bit.ly/1k2hxUv)

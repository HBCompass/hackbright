Exercise 01: Conditionals, variables
=======

Tutorials & Resources:
-------
Take a look at these online resources before you attempt this exercise. If you get stuck, check the work you've already completed. Do these before starting the exercise below.

* http://learnpythonthehardway.org/book/ex6.html
* http://learnpythonthehardway.org/book/ex7.html
* http://learnpythonthehardway.org/book/ex11.html
* http://learnpythonthehardway.org/book/ex29.html
* http://learnpythonthehardway.org/book/ex30.html
* http://learnpythonthehardway.org/book/ex31.html
* http://learnpythonthehardway.org/book/ex33.html

Concepts required:
* while loops
* 'break' statement
* conditionals
* user input
* formatting strings
* the int() function

Introduction
-------
Programs tend to be structured around a 'main loop', which repeatedly executes the primary task of the program. It is important to understand that the primary task is not necessarily the primary function of the program. As an example, the primary function (or at least, the primary usage) of the program 'cat' is to print the contents of a file to the screen. However, the primary task in accomplishing that is printing individual lines of the file in sequence. In pseudocode, it might look like this:

    f = open_file(filename)
    for each line 'l' in file 'f':
        print l

Consider a calculator program, that lets you enter arithmetic expressions, then evaluates and prints the output until you tell it to quit. It might look like this:

    while True:
        expression = read_input()
        value = evaluate_expression(expression)
        print value

In general, a program is structured like this:

    do_setup()
    while exit_condition_not_reached:
        input = consume_input()
        output = evaluate_input(input)
        print output

In the case of 'cat', input comes from the file specified on the command line. In the calculator, input comes from the keyboard.


Description
-------
Write a program named guess.py that plays the 'number guessing game'. The computer will choose a random number between 1 and 100, and ask the user to guess the number, giving them a hint if it's high or low. A sample game looks like this:

```
Meringue:guessing chriszf$ python ./guess.py 
Howdy, what's your name?
(type in your name) Christian
Christian, I'm thinking of a number between 1 and 100. Try to guess my number.
Your guess? 50
Your guess is too low, try again.
Your guess? 80
Your guess is too high, try again.
Your guess? 60
Your guess is too low, try again.
Your guess? 70
Your guess is too high, try again.
Your guess? 63
Your guess is too low, try again.
Your guess? 64
Your guess is too low, try again.
Your guess? 67
Your guess is too low, try again.
Your guess? 69
Your guess is too high, try again.
Your guess? 68
Well done, Christian! You found my number in 9 tries!
```

A rough pseudocode outline of the program will look like this:

    greet player
    get player name
    choose random number between 1 and 100
    while True:
        get guess
        if guess is incorrect:
            give hint
        else:
            congratulate player

            
Version Control (git)
-------
While you're writing your code, try and remember to use 'git' at various points to save your progress.  If you've never used version control before, it's a lot like enabling "Track Changes" in a Microsoft Word document.  Every time you "commit" your code, you're saving a snapshot in time.  If you make a change you don't like or mess something up, you can rollback to a previous commit.

For those of you who play adventure games, the moto "Save Early, Save Often" should come to mind.

So if you take the rough pseudocode outline from above, you'll probably want to go about creating your program in the following order:

1. Create a new folder/directory to store your project
1. Create your project file.  "subl guessing.py" will probably get you started.  ;)
1. Have your code greet the player.
1. Test your code!  Does it greet the player?
1. Time to save!
  1. git init
  1. git status
  1. git add guessing.py
  1. git status
  1. git commit -m "Greeting the Player"
  1. git status
1. Ok, on to the next step!  Get the player's name.
1. Test your code!
1. Does it work?  Time to save!
  1. git status
  1. git add guessing.py
  1. git status
  1. git commit -m "Getting the Player's Name"
  1. git status
1. Sensing a pattern yet?  Repeat for the next steps, testing your code at each step.  When you have a step working, save it!
 
As you get more comfortable with git, you won't need to do a 'git status' at every step.  We're only having you do that here so you can see what is happening at each step and get used to the messages that git returns.

## Go Back!

At some point, if you didn't make a mistake in your code, go ahead and break something (though make sure you've commited your working code before you go breaking things).

So if you're code is broken or you explored an idea that didn't turn out the way you wanted it to and you just want to go back to your last commit, try:

    git reset --hard HEAD

*WARNING:* This will erase any changes you have not committed, so please use with care!


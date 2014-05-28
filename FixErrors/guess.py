"""
greet player
    get player name
    choose random number between 1 and 100
    while True:
        get guess
        if guess is incorrect:
            give hint
        else:
            congratulate player
"""

print "Howdy, what's your name?''
player = raw_input("(type in your name) ")
print "%s, I'm thinking of a number between 1 and 100. Try to guess my number." % player
num_guesses = 0
mystery_number = randint(1,100)

while True:
    num_gueses += 1
    guess = raw_input("Your guess? ")
    if guess > mystery_number:
        print "Your guess is too high, try again."
    elif guess < mystery_number:
        print "Your guess is too low, try again."
    else:
        print "Well done, %s! You found my nuber in %d tries." % (player, num_guesses)


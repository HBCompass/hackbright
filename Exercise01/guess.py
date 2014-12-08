#Pair Programming - Partnered with Caroline Orsi

#import the random module to get random numbers
import random

#asks user for their name
print "Why hello there, what's your name?"
name = raw_input("> ")

#set the high score
highscore = 1000

#defines the function for a single game
def guess():     
    print ("%s , I'm thinking of a number between 1 and 100. Try "
    "to guess my number." % name)     
    
    #creates a variable for the random number within the range and defines score variable
    num = random.randint(0, 100)     
    score = 0
    
    #declares global variable highscore
    global highscore

    #gets number from user and tests if it's a valid entry
    while True:
        guess = raw_input("> ")
        try:
            guess = int(guess)
        except ValueError:
            print ("That is not a number!")
            continue

        if guess < 1 or guess > 100:
            print ("Enter a number between 1 and 100")
            continue
            
        score += 1
        if guess < num:
            print "Your guess is too low, try again."
        elif guess > num:
            print "Your guess is too high, try again."
        else:    
            print "You got it! You tried %d times." % score
            if score < highscore:
                highscore = score
                print "You beat the high score! The new high score is %d" % highscore
            break

#defines the function to repeat gameplay
def gameplay():
    playagain = "yes"

    while playagain == "yes":
        guess()

        print "Would you like to play again? Enter yes or no."

        playagain = raw_input("> ").lower()
   
    print "Thanks for playing!"


#gives the initial call to start the game
gameplay()

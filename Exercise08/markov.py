#Pair Programming - partnered with Lauren Chow

#!/usr/bin/env python

#import sys
import random


import twitter

#tapi = twitter.Api()


#print tapi.VerifyCredentials()

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    
# This section reads the corpus file in to the program and splits the words in a words list.     
    text = corpus.read() #this is functionally the same as the more complicated stuff below
    words = text.split()

    chain_dict = {}
    """
    for line in f:
        line = line.rstrip()
        words.extend(line.split())
     """   
#This looks at each word entry in the list that we made from original text - if the tuple does not yet exist,
#it appends it to the dictionary as a key. If it does exist, it appends the value to the existing key.

    for each_number in range(len(words)-2): 
        if (words[each_number], words[each_number+1]) not in chain_dict.keys():
            chain_dict[(words[each_number], words[each_number+1])] = [words[each_number+2]]
        else:
            chain_dict[(words[each_number], words[each_number+1])].append(words[each_number+2])
    
    return chain_dict

def make_text(chain_dict):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

# This selects the first random key to begin the chain.
    
    random_key = random.choice(chain_dict.keys())

# This creates a random text list to append a random value from the original random key.
# The random key is then reassigned to a tuple containing the second key in the random keys tuple,
# and adds the randomly generated value of the earlier random key tuple as the second tuple value. 
# Convert tuples in random_key to strings, then added all strings together, then added to empty list

    first_words = ' '.join(map(str,random_key)) 
    random_text_list = [first_words]
    
    for i in range(1,100):
    #while random_key in chain_dict:    
        next = random.choice(chain_dict[random_key]) 
        random_text_list.append(next)
        random_key = (random_key[1],next)

    pretty_text = []
    pretty_text = ' '.join(map(str, random_text_list)) 
    return pretty_text
        
    
 #This is taking all the entries in random_text_list and adding them together as one string separated
 #by a space each time, then returning this list to the main function to print.


def main():

#    args = sys.argv

    input_text = open("jaggedlittlephil.txt")

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    twitter_text = random_text[0:130]

    last_space=twitter_text.rfind(' '[0:130])
    #print "Here's your text %s" % twitter_text
    #print "Here's where the last space is %r" % last_space
    #print "This will be last letter of last full word %s" % twitter_text[last_space-1]

    truncated_text = twitter_text[0:last_space]
    print truncated_text
 
    #status = tapi.PostUpdate(truncated_text + " #sussudio")
    #print status.text     
     

if __name__ == "__main__":
    main()
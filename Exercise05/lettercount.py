#Read a text file and count the number of occurences for each letter in the file

import string
# Opens the file and reads it into a string before closing then file
f = open("twain.txt")
graphs = f.read()
f.close()

# Converts all of the text to lowercase 
graphs = graphs.lower()

# Creates a list of the letters in the alphabet
letters = list(string.ascii_lowercase)

# Creates an empty list to append the counts to
letter_count = []

for i in range(len(letters)): # Looks at the list of letters in the alphabet
 	letter_count.append(0) 

# Looks at the characters in graphs
for char in graphs:
# For a character in graphs is also in letters, it gets appended to letter_count			
 	if char in letters:		
# Each new instance gets
 		letter_count[letters.index(char)] += 1

print letter_count
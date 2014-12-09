from collections import Counter

# Opens file assigns words to list.

f = open("twain.txt")
graphs = f.read()

# text = graphs.lower().split()

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

no_punct = ""

for char in graphs:
	if char not in punctuations:
		no_punct = no_punct + char

text = no_punct.lower().split()

tally = Counter(text)
print tally
















# for i in range(len(text)):
# 	word = text[i]
# 	for char in word:
# 		if char in string.
# 			word = word.replace(char,"")
# 	text[i] = word
      
# print word
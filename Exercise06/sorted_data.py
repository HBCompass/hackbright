# Opening the file and assigning the restaurant name and rating to lists.    

name = []
score = []

f = open("scores.txt")

for line in f:
    entries = line.split(':') 
    name.append(entries[0])
    score.append(entries[1])

ratings_dict = dict(zip(name,score))

keys_list = ratings_dict.keys()

keys_list.sort()

for key in keys_list:
    print "Restaurant %s received a rating of %s." % (key, ratings_dict[key])
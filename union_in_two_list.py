i = ['a','b','c']
j = ['b','d']

for x in i: # loop through list i put in x
    if x in j: # if items in x are in list j print x is the variable that holds results
        print(x)

both = list()   # an empty list
for a in i:     # get all items to a in i (list)
    for b in j: # get all items to b in j (list)
        if a == b: # if present item a equal b Add to to a list called both
            both.append(a)
print("common item : {}".format(both)) #printing a common item


c = [a for a in i if a in j]
print(c)


b = list(set(i).intersection(j)) #intersection is an python method | (∩) symbol of intersection
print(b)

n = [a for a in i if a in j and(j.pop(j.index(a)) or True)]
print(n)

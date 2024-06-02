import numpy as np

def alphabetical_value(name):
    """
    Returns the sum of the letter values in the name.
    """
    res = 0
    for letter in name:
        res += (ord(letter) - ord("A") + 1)
    return res

input = open("names.txt")
text = input.read()
names = text.split(",")
names = [name[1:-1] for name in names]
names.sort()

score = 0
for i in range(len(names)):
    score += (i+1) * alphabetical_value(names[i])
print(score)

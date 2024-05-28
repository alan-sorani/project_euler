import numpy as np

# take input string from file and separate it into a list of numbers
input = open("input.txt", "r")
input = input.read()
input = input.split("\n")
if(input[-1] == ""):
    input = input[0:-1]
input = [int(number) for number in input]

# take the sum of the numbers, then take its first 10 digits
sum = np.sum(input)
res = str(sum)[0:10]
print(res)

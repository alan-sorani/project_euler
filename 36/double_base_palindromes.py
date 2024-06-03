import numpy as np

sum = 0
for i in range(1,1000000):
    i_decimal = str(i)
    i_binary = bin(i)[2:]
    if((i_decimal == i_decimal[::-1]) and (i_binary == i_binary[::-1])):
        sum += i
print(sum)

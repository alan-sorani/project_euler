from itertools import permutations

'''
We do this straightforward, by considering from the get-go polydigital numbers.
'''

pandigitals = [''.join(p) for p in permutations('1234567890')]
res = 0
for pandigital in pandigitals:
    if(pandigital[0] == '0'):
        continue
    if(int(pandigital[3]) % 2 != 0):
        continue
    if(int(pandigital[2:5]) % 3 != 0):
        continue
    if(int(pandigital[5]) not in {0,5}):
        continue
    if(int(pandigital[4:7]) % 7 != 0):
        continue
    if(int(pandigital[5:8]) % 11 != 0):
       continue
    if(int(pandigital[6:9]) % 13 != 0):
       continue
    if(int(pandigital[7:]) % 17 != 0):
       continue
    res += int(pandigital)

print(res)

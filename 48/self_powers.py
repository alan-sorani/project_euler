import numpy as np

'''
The last ten digits of a number are its value mod 10**10.

If m is a multiple of ten, we get :math:`m^m \equiv 0 \mathrm{mod} 10^10`, so such numbers don't affect the last digits.
'''

def mod_power(n : int, k : int, m : int):
    '''
    Computes n**k mod m.
    '''
    if(k == 0):
        return 1
    if(k == 1):
        return n % m
    res = 1
    i = k
    while(i > 0):
        res *= n
        res = res % m
        i -= 1
    return res

print(int(np.sum([mod_power(i,i,10**10) for i in range(1,1001)])) % 10**10)

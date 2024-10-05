from decimal import Decimal, getcontext
from math import sqrt

def sum_root_decimals(num : int) -> int:
    if(num == int(sqrt(num+0.0005))**2):
        return 0
    num_decimal = Decimal(num)
    root = num_decimal.sqrt()
    root_str = str(root)
    digits = list(''.join(root_str.split(".")))[:100]
    return sum([int(digit) for digit in digits])


if __name__ == "__main__":
    getcontext().prec = 120
    res = 0
    for i in range(2,100):
        sqrt_digit_sum = sum_root_decimals(i)
        print(i, sqrt_digit_sum)
        res += sqrt_digit_sum
    print(res)


import numpy as np

def digits(num : int):
    return set(str(num))

def test_permutations(num : int):
    num_digits = digits(num)
    for i in range(2,7):
        if(digits(i * num) != num_digits):
            return False
    return True

if __name__ == "__main__":
    num = 10**5
    while(True):
        if(test_permutations(num)):
            break
        num += 1
    print(num)

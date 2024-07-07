import numpy as np

def reverse_num(num : int):
    return int(''.join(list(str(num))[::-1]))

def test_lychrel(num : int):
    temp = num
    for step in range(49):
        temp = temp + reverse_num(temp)
        if(temp == reverse_num(temp)):
            return True
    return False

if __name__ == "__main__":
    count = 0
    for i in range(1, 10000):
        count += not test_lychrel(i)
    print(count)

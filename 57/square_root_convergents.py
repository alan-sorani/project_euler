from fractions import Fraction

# We notice that if :math:`a_n` is the :math:`n`th approximation of :math:`\sqrt(2)`, then one has the recurrence formula :math:`a_n = (a_{n-1} + 1)^{-1} + 1`.

def num_digits(num : int) -> int:
    return len(str(num))

if __name__ == "__main__":
    a = Fraction(3/2) 
    count = 0
    
    for n in range(1,1001):
        count += num_digits(a.numerator) > num_digits(a.denominator)
        a = 1 / (a + 1) + 1

    print(count)

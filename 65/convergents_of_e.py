from fractions import Fraction

if __name__ == "__main__":
    # We construct the fraction from "bottom to top", which is easier to compute.
    continued_fraction_digits = [1] + [int(2 * (i/3 + 1)) if i % 3 == 0 else 1 for i in range(99)][:-1]
    digits = continued_fraction_digits[::-1]
    convergent = digits[0]
    i = 1
    while(i < len(digits)):
        convergent = Fraction(1, convergent)
        convergent += digits[i]
        i += 1
    convergent = Fraction(1, convergent)
    convergent += 2
    print(sum([int(digit) for digit in str(convergent.numerator)]))

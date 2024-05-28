import numpy as np

# instead of looking at all the numbers separately and counting the number of letters in them, we count the letters in different expressions and multiply by how many times they appear

units = ["one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine"]
teens = ["ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen"]
tens = ["twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety"]
hundreds = [digit + "hundred" for digit in units]

units = np.array([len(num) for num in units])
teens = np.array([len(num) for num in teens])
tens = np.array([len(num) for num in tens])
hundreds = np.array([len(num) for num in hundreds])

# each units digit appears 9 * 10 times when the tens digit is not 1 
units_count = 9 * 10
units_res = np.sum(units_count * units)

# teens appear once for each hundreds digit
teens_count = 10
teens_res = np.sum(teens_count * teens)

# tens appear once for each combinations of units digit and hundreds digit
tens_count = 10 * 10
tens_res = np.sum(tens_count * tens)

# hundreds appear 100 times each
hundreds_count = 100
hundreds_res = np.sum(hundreds_count * hundreds)

# the word "and" appears once for each number from 100 to 999, except for multiples of 100
and_res = (999 - 99 - 9) * 3

# "one thousand" appears once
thousands_res = len("onethousand")

res = units_res + teens_res + tens_res + hundreds_res + and_res + thousands_res

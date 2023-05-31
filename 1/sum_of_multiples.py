from itertools import product
from functools import reduce

"""
product_set

Input: a set s of numbers and a number n
Output: the set of products of the form s_1 * s_2 ... * s_n where s_i are different numbers in s
"""
def product_set(s, n):
	return {reduce(lambda x,y:x*y,p) for p in product(s,repeat=n) if len(p)==len(set(p))}

"""
sum_of_multiples

Input: a set factors_set of prime factors and a maximum number max_num

Output: the sum of all multiples of any of the factors that are less than or equal to the maximum number

Proof: We want to count each multiple of the numbers exactly once.
We count each number m once for each of its factors in factors_set, then substract (n choose 2) where n is its number of factors in factor_set, as this is the number of products of primes from factor_set which divide m then add (n choose 3) and so on. We get
sum_{k=1}^n (n choose k) (-1)^{k-1} = - sum_{k=1}^n (n choose k) (-1)^k = 1 + sum_{k=0}^n (n choose k) (-1)^k = 1 + (1-1)^n = 1
"""
def sum_of_multiples(factor_set, max_num):
	result = 0
	for i in range(1,len(factor_set)+1):
		product_factor_set = product_set(factor_set,i)
		for factor in product_factor_set:
			min_factor = factor
			num_summands = int(max_num/factor)
			max_factor = factor * num_summands
			result += (-1)**(i+1) * (min_factor + max_factor) * num_summands / 2 
	return result

"""
pythagorean_triplet_sum

    Input: a number, sum
    Output: an array of all pythagorean triplets (a,b,c) such that a+b+c = sum, where a<b<c and a^2 + b^2 = c^2.
"""
def pythagorean_triplet_sum(sum):
    results = []
    max_range = int(sum/2)+1
    for a in range(1,max_range):
        for b in range(a,max_range):
            c = (a**2 + b**2)**0.5
            if(c != int(c)):
                continue
            if(a+b+c == sum):
                results += [(a,b,c)]
    return results

import numpy as np

'''
The area of a triangle with sides a,a,b is :math:`\sqrt{a^2b^2 - \frac{b^2}{4}}`, as is computed by placing the length b orthogonal to the x-axis with the vertex in front of it at (0,0), and using trigonometry.
For this value to be an integer n, we get that :math:`16 n^2 = 4 a^2 b^2 - b^4`, so that b has to be of the form 2m for m an integer. Substituting b=2m, we get that the area is integral if and only if :math:`m^2(a^2 - m^2) = n^2` is a square integer. Since :math:`m^2, (a^2 - m^2)` are both integers, and since :math:`m^2` is a square, this is equivalent to :math:`a^2 - m^2 = a^2 - \left(\frac{b}{2}\right)^2` being a square.
'''

max_perimeter = 1_000_000_000
a = 3
res = 0
while((a-1)*3 <= max_perimeter):
    for b in {a-1, a+1}:
        test = np.sqrt(a**2 - (b/2)**2) 
        if(test == int(np.rint(test))):
            print(f"({a},{a},{b}): {np.sqrt(a**2 * b**2 / 4 - b**4/16)}")
            res += 2*a + b
    # since b has to be even, a has to be odd
    a += 2
print(res)

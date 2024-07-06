import numpy as np
from time import time

'''
Consider P,Q as vectors in :math:`\mathbb{R}^2`, and assume that P has a smaller angle than Q above the x-axis.

There are 3 cases for the right angle:
    1. OPQ
    2. PQO
    3. QOP

In the third case, we must have that :math:`P,Q` lie on the :math:`x,y` axes respectively, so that number of options in that case is :math:`50^2`, the number of options for choosing the coordinates :math:`P_1, Q_2`.

For each triangle in the third case, we get a triangle with right-angle OPQ by reflecting through :math:`x = P_1/2`, and a triangle with right-angle PQO by reflecting through :math:`y = Q_2/2`.

We are left with triangles with :math:`P_1, P_2 \neq 0` such that the right-angle is OPQ, and with their reflections through the `y = x` line.

For counting these, we note that OPQ being a right angle means exactly that Q-P is orthogonal to P. We thus need to find P = (P_1, P_2) such 1 <= P_1, P_2 <= 50, and H = (H_1, H_2) such that H_1 * P_1 + H_2 * P_2 = 0 and also P_1 + H_1 >= 0 and P_2 + H_2 <= 50.

For such values we get :math:`H_1 = -(H_2 \cdot P_2) / P_1`. Writing :math:`h = H_2` we get the requirements :math:`h \leq 50 - P_2` and :math:`-(h \cdot P_2) / P_1 = H_1 \geq -P_1`, where the latter is equivalent to :math:`h \leq P_1^2 / P_2`.

Also, for every :math:`h` we have that :math:`H = (-\frac{h P_2}{P_1}, h)` is orthogonal to :math:`P`, so we want for each choice of :math:`P_1, P_2` to count the number of integers :math:`1 \leq h \leq \min(50 - P_2, \frac{P_1^2}{P_2})` for which :math:`\frac{h P_2}{P_1}` is an integer.

This is an integer exactly if :math:`h \in \frac{P_1}{P_2} \mathbb{N}_+`. Let :math:`d = \mathrm{gcd}(P_1, P_2)` and :math:`A_i = P_i / d`. We have that `h \in \frac{P_1}{P_1} \mathbb{N}_+ \cap \mbb{N}_+` if and only if :math:`h` is an integer multiple of `A_1`, since :math:`m A_1 \equiv 0 (\mathrm{mod} A_2)` can only happen when :math:`A_2 \mid m`, due to :math:`A_1, A_2` being coprime.

Hence, we have to count elements :math:`h in A_1 \mathbb{N}_+` such that :math:`1 \leq h \leq \min(50 - P_2, \frac{P_1^2}{P_2})`.
'''

def count_right_triangles(max_coordinate : int):
    """
    Counts the number of right triangles with integer coefficients between 0 and a given number.
    """
    res = np.sum([
        np.floor(
            np.min([
                max_coordinate-P2,P1**2 / P2
            ]) / np.gcd(P1, P2)
        ) for P1 in range(1,max_coordinate+1) for P2 in range(1,max_coordinate+1)
    ])
    res = 2 * res + 3 * max_coordinate ** 2
    return res

if __name__ == "__main__":
    t_0 = time()
    print(count_right_triangles(50))
    print(f"Computed in {time() - t_0} seconds.")

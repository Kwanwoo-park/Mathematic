from matplotlib_venn import venn2
import matplotlib.pyplot as plt
from sympy import FiniteSet


def draw_venn(sets):
    venn2(subsets=sets)
    plt.show()


def check_prime(n):
    prime = []
    a = [False, False] + [True]*(n-1)

    for i in range(2,n+1):
        if a[i]:
            prime.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False

    return prime


s1 = FiniteSet(*range(1, 20, 2))
s2 = FiniteSet(*check_prime(20))

draw_venn([s1, s2])
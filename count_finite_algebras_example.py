"""
Example use of the count_finite_algebras tool.

Charlotte Aten (caten2@u.rochester.edu) 2016
"""

import sage.all
from count_finite_algebras import *
from sage.rings.arith import factor

print("Dislpay a tuple of all partitions of the natural number `i` from 1 through 6.")
for n in range(1,6):
    print(partition(n))
print("")

print("Display the cycle counts for each partition of 4.")
for part in partition(4):
    print([part,cycle_count(part, 4)])
print("")

print("Display the summand for each of the partitions of 4.")
for part in partition(4):
    print("The summand for {} is {}.".format(part,summand(part,4)))
print("")

print("For `n` from 1 through 10 show the number `c` of isomorphism classes of magmas of order `n`")
print("as well as the prime factorization of `c`.")
for n in range(1,11):
    c = finite_algebra_count(n)
    print((n,c,factor(c)))
"""
Tool for counting the number of isomorphism classes of finite magmas of a given order.

Uses SageMath (sagemath.org).

See "The Number of Isomorphism Types of Finite Algebras" (1966) by Michael A. Harrison for
a derivation of the technique used here.

Generates sequence listed as A001329 in the Online Encyclopedia of Integer Sequences (oeis.org/A001329). 

Charlotte Aten (caten2@u.rochester.edu) 2016
"""

import sage.all
from math import factorial
from sage.rings.arith import divisors, lcm, gcd, prod

def partition(n):
    """
    Return a dictionary of partitions of a natural number `n`.

    Args:
        n (int): The number to be partitioned.

    Returns:
        dict: The partitions of `n`, up to reordering.
    """

    i = 1
    dic = {1: ([1],)}
    while i != n:
        newlis = []
        for j in xrange(1,i+1):
            for entry in dic[j]:
                part = entry[:]
                part.insert(0,i+1-j)
                newlis.append(part)
        newlis.append([i+1])
        dic[i+1] = tuple(newlis)
        i += 1
    return dic[n]

def cycle_count(part, n):
    """
    Create a tuple of the number of `r`-cycles in a given partition of `n`.

    Args:
        part (tuple): A partition of `n` represented as a tuple.
        n (int): The integer for which `part` is a partition.

    Returns:
        tuple: A tuple whose `r`-1 is the number of `r`-cycles in `part`.
    """

    return tuple(part.count(r) for r in xrange(1,n+1))

def summand(part, n):
    """
    Create the summand used in the Harrison count for a given partition.

    Args:
        part (tuple): A partition of `n` represented as a tuple.
        n (int): The integer for which `part` is a partition.

    Returns:
        int: The summand corresponding to the partition `part` of `n`.
    """

    t = 1
    count = list(cycle_count(part, n)) + (factorial(n)-n)*[0]
    for i in range(1,n+1):
        for j in range(1,n+1):
            s = sum([d*(count[d-1]) for d in divisors(lcm(i,j))])
            t = t*(s**(count[i-1]*count[j-1]*gcd(i,j)))
    t = t*factorial(n)/(prod(factorial(count[d-1])*(d**(count[d-1])) for d in range(1,n+1)))
    return t

def finite_algebra_count(n):
    """
    Perform Harrison's count of the number of finite magmas of order `n` up to isomorphism.

    Args:
        n (int): The order for which to count isomorphism classes.

    Returns:
        int: The number of isomorphism classes of magmas of order `n`.
    """

    found_cycles = []
    parts = []
    for part in partition(n):
        if cycle_count(part, n) not in found_cycles:
            found_cycles.append(cycle_count(part, n))
            parts.append(part)
    return sum([summand(part, n) for part in parts])/factorial(n)
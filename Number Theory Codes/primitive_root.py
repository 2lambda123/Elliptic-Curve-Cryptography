# python code for calculating the primitive roots of a prime number n.
# given a prime number n, find if there are primitive roots modulo n.
# If yes, then outputting the smallest primitive root.
# If 'a' is a primitive root, then a^(p-1/2) == -1 mod (p).
# Depending upon the value of MAX, the program works for larger values.

# 104729 is the 10,000-th prime number - approx 2 seconds on M1 MacBook Pro
# 1299709 is the 100,000-th prime number - approx 33 seconds on M1 MacBook Pro
# 15485863 is the 1,000,000-th prime number - approx 370 seconds on M1 MacBook Pro

# the number of prime numbers less than a certain number
'''
MAX    Pi
10    4     The four prime numbers less than 10 are: 2, 3, 5, 7
100    25
1 000    168
10 000    1 229
100 000    9 592
1 000 000    78 498
10 000 000    664 579
100 000 000    5 761 455
1 000 000 000    50 847 534     There are 50 million primes with 9 digits (in base 10)
'''

import math
import sys
import mod_exp
import rsa
import time
# the time module is to check for the time taken to run the program


Machine = sys.maxsize
MAX = 15485863
num_list = [i for i in range(MAX)]


# A precalculated smallest prime factors
# O(n.log(log n)) -> Time Complexity
def sieve(N):
    for i in range(4, N, 2):
        num_list[i] = 2
    for i in range(3, math.ceil(math.sqrt(N))):
        if num_list[i] == i:
            for j in range(i * i, N, i):
                if num_list[j] == j:
                    num_list[j] = i


# O(log n) -> Time Complexity
def p_factors(P):
    primes = []
    while P != 1:
        primes.append(num_list[P])
        P = P // num_list[P]
    return primes


# O(n.log Φ(n).log n) -> Time Complexity
def small_p_root(P, N):
    phi = rsa.euler_totient(P, 2)
    sieve(N)
    primes = p_factors(phi)
    for i in range(1, P):
        newL = []
        for j in primes:
            exp = int(phi / j)
            newL.append(mod_exp.modular_exponentiation(i, exp, P))
        if newL.count(1) == 0:
            print(f'Smallest primitive root of {P} is: {i}')
            break


# O(n.log Φ(n).log n) -> Time Complexity
def all_p_roots(P, N):
    phi = rsa.euler_totient(P, 2)
    sieve(N)
    primes = p_factors(phi)
    p_roots = []
    for i in range(1, P):
        newL = []
        for j in primes:
            exp = int(phi / j)
            newL.append(mod_exp.modular_exponentiation(i, exp, P))
        if newL.count(1) == 0:
            p_roots.append(i)
    print(f'{P} has {len(p_roots)} primitive roots')
#    print(f'All primitive roots of {P} are: ')
#    print(*p_roots, sep=', ')



p = int(input("Prime Number p: "))
if rsa.isprime(p) != 1:
    sys.exit("ERROR: Input number is not a prime...\nTerminating the program")
elif p > 15485863:
    sys.exit("ERROR: Input prime is too large, try primes less than (15485863)...\nTerminating the program")
else:
    start = time.process_time()
    factor = pow(p, 2)
    factor = p + 1
    all_p_roots(p, factor)
    small_p_root(p, factor)

TIME = time.process_time() - start
print(f'Time taken to execute the program {round(TIME, 4)} s')

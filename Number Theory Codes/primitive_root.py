# python code for calculating the primitive roots of a prime number n.
# given a prime number n, find if there are primitive roots modulo n.
# If yes, then outputting the smallest primitive root.
# If 'a' is a primitive root, then a^(p-1/2) == -1 mod (p).
# Depending upon the value of MAX, the program works for larger values.


import math
import sys
import mod_exp
import rsa


Machine = sys.maxsize
MAX = 10000001
num_list = [i for i in range(MAX)]


# A precalculated smallest prime factors
# O(n.log(log n)) -> Time Complexity
def sieve():
    for i in range(4, MAX, 2):
        num_list[i] = 2
    for i in range(3, math.ceil(math.sqrt(MAX))):
        if num_list[i] == i:
            for j in range(i * i, MAX, i):
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
def small_p_root(P):
    phi = rsa.euler_totient(P, 2)
    sieve()
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
def all_p_roots(P):
    phi = rsa.euler_totient(P, 2)
    sieve()
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
    # print(f'All primitive roots of {P} are: ')
    # print(*p_roots, sep=', ')


if __name__ == '__main__':
    p = int(input("Prime Number p: "))
    if rsa.isprime(p) != 1:
        print("ERROR: Given number is not a prime")
        exit()
    else:
        small_p_root(p)
        all_p_roots(p)

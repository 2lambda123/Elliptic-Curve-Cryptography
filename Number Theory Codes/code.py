# The 105,098,565th prime is 2,147,504,921.
# The 105,098,564th prime is 2,147,504,911.
# 2^31 is 2,147,483,648.
# 2^31-1 is prime -> 2,147,483,647 -> The 105,097,565th prime
# The 105,097,564th prime is 2,147,483,629.


import sys
from math import sqrt
from typing import Tuple

def isprime(N):
    flag = 1
    for i in range(2, int(sqrt(N)) + 1):
        if N % i == 0:
            flag = 0
            break
    else:
        return flag


def euler_totient(p1, p2):
    return (p1-1)*(p2-1)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


p1 = int(input("Enter p1: "))
p2 = int(input("Enter p2: "))

if isprime(p1) == 0:
    sys.exit("p1 not prime")
if isprime(p2) == 0:
    sys.exit("p2 not prime")

n = p1 * p2
phi_n = euler_totient(p1, p2)

for a in range(2, phi_n):
    if gcd(a, phi_n) == 1: break
    
b = pow(a, -1, phi_n)

print(f'Prime p1 -> {p1}')
print(f'Prime p2 -> {p2}')
print(f'Product n -> {n}')
print(f'Euler Totient phi_n -> {phi_n}')
print(f'Value of a, gcd(a, phi_n) = 1 -> {a}')
print(f'Value of b, inverse mod of a, phi_n = {b}')

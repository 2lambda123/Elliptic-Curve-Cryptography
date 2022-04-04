# encryption and decryption of RSA Crypto-system
# the system limit is 16bit OS 4B
import sys
import random
from math import sqrt
from typing import Tuple

sys.setrecursionlimit(1000000000)


# Checking whether the given number is prime or not
# Time Complexity - O(sqrt(n))
def isprime(N):
    flag = 1
    for i in range(2, int(sqrt(N)) + 1):
        if N % i == 0:
            flag = 0
            break
    else:
        return flag


# Returns the Euler Totient Value of a given number
def euler_totient(p1, p2): return (p1 - 1) * (p2 - 1)


# Finding GCD using Basic Euclidean Algorithm
# Time Complexity - O(log(min(a, b)))
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# Calculating the value of a^n mod(m) using Modular Exponentiation
# Time Complexity - O(log n)
def mod(a, n, m):
    term = a
    binary_n = format(n, "b")
    # binary_n = "".join(reversed(binary_n))
    b0 = binary_n[-1]
    if b0 == '1':
        product = a
    else:
        product = 1
    for b in reversed(binary_n[:-1]):
        term = (term * term) % m
        if b == '1':
            product = (product * term) % m
    return product


# Extended Euclidean Algorithm
# d = gcd(a, b) = x*a + y*b; returns x and y
def egcd(a, phi_n) -> Tuple[int, int, int]:
    if a == 0:
        return phi_n, 0, 1
    else:
        b_div_a, b_mod_a = divmod(phi_n, a)
        # divmod() returns quotient and remainder
        g, x, y = egcd(b_mod_a, a)
        return g, y - b_div_a * x, x


# Calculating the value of a^-1 mod(m) using Extended Euclidean Algorithm
# Time Complexity - O(log m)
def inverse_mod(a, phi_n):
    g, x, _ = egcd(a, phi_n)
    if g != 1:
        raise Exception(f'gcd({a}, {phi_n}) != 1')
    return x % phi_n


def encrypt():
    sys.stdout.write("NOTE: For whitespace, type '-'\n")
    try:
        message = input("Enter the text that is to be encrypted: ")
        message.split('-')
        encrypted = []
        p1 = int(input("Enter the prime p1: "))
        if isprime(p1) != 1:
            print(f'The number {p1} is not a prime number')
            exit()
        p2 = int(input("Enter the prime p2: "))
        if isprime(p2) != 1:
            print(f'The number {p2} is not a prime number')
            exit()
        n = p1 * p2
        phi_n = euler_totient(p1, p2)
        relatively_prime = []
        for a in range(2, phi_n):
            if gcd(a, phi_n) == 1:
                relatively_prime.append(a)
        rand = int(random.random() * len(relatively_prime))
        a = relatively_prime[rand]
        for msg in message.split('-'):
            encrypted.append(mod(int(msg), a, n))
        sys.stdout.write("The encrypted message is: \n")
        print(*encrypted, sep="-")
        print(f'Public Keys = {a} and {n}')
    except:
        sys.stdout.write("Unknown Error Occurred during encryption\n")
        exit()


def decrypt():
    sys.stdout.write("NOTE: For whitespace, type '-'\n")
    try:
        message = input("Enter the text that is to be decrypted: ")
        message.split('-')
        decrypted = []
        sys.stdout.write("Decryption of RSA Crypto-system requires 2 Public Keys, 'a' and 'n'\n")
        a = int(input("Enter the value of a: "))
        n = int(input("Enter the value of n: "))
        p1 = 0
        for p in range(2, int(sqrt(n)) + 1):
            if n % p == 0:
                p1 = p
                break
        p2 = int(n / p1)
        phi_n = euler_totient(p1, p2)
        if gcd(a, phi_n) != 1:
            print(f'ERROR: The key \'{a}\' cannot be a Public Key for this RSA System\n')
            exit()
        else:
            b = inverse_mod(a, phi_n)
            print(f'Inverse Modulo of {a}, ϕ({n}) = {b}')
            for msg in message.split('-'):
                decrypted.append(mod(int(msg), b, n))
            sys.stdout.write("The decrypted message is: \n")
            print(*decrypted, sep="-")
            print(f'Private Keys = {p1}, {p2}, and {b}')
    except:
        sys.stdout.write("Unknown Error Occurred during decryption\n")
        exit()


if __name__ == '__main__':
    sys.stdout.write("The Program only works for numbers. Still in development phase\n")
    sys.stdout.write("The system encrypts and decrypts only unto 16bit OS 4B\n")
    sys.stdout.write("For Encrypting the message Press e/E\n")
    sys.stdout.write("For Decrypting the message Press d/D\n")
    key = input("Press any key to perform action: ").upper()
    if key == 'E':
        encrypt()
    elif key == 'D':
        decrypt()
    else:
        sys.stdout.write("Error: Keyboard Interruption (Wrong Key Pressed)\n")
        exit()

# encryption and decryption of RSA Crypto-system
# the system limit is 64bit
import sys
import random
from math import sqrt, log2
from typing import Tuple


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


# generate prime numbers from 2 to 1,000,000th prime number
def key_generator():
    primes = []
    file = open('primes.txt', 'r')
    for p in file.read().split(', '):
        primes.append(int(p))
    file.close()
    cipher = random.randint(1, 100)
    p1_idx = random.randint(0, len(primes)-1)
    p2_idx = random.randint(0, len(primes)-1)
    while p2_idx == p1_idx:
        p2_idx = random.randint(0, len(primes)-1)
    return (primes[p1_idx], primes[p2_idx], cipher)


# the function first encodes the message, and then encrypts
def encrypt():
    try:
        message = input("Enter the text that is to be encrypted: ")
        encrypted = []
        sys.stdout.write("Message encoding successful\n")
        p1, p2, c = key_generator()
        n = p1 * p2
        phi_n = euler_totient(p1, p2)
        a = phi_n // c
        while gcd(a, phi_n) != 1:
            a -= 1
        for msg in message:
            encrypted.append(pow(int(ord(msg)+c), a, n))
        sys.stdout.write("Message encryption successful\n")
        sys.stdout.write("The encrypted message is: \n")
        print(*encrypted)
        print(f'Public Keys = ({a}, {n})')
        print(f'Cipher Key = {c}')
    except:
        sys.exit("\nERROR: Encryption failed...\nTerminating the program")


# the function just decrypts the message but doesn't decode
def decrypt():
    try:
        message = input("Enter the text that is to be decrypted: ")
        message = message.split()
        decrypted = []
        sys.stdout.write("Decryption of RSA Crypto-system requires 2 Public Keys, 'a' and 'n'\n")
        a = int(input("Enter the value of a: "))
        n = int(input("Enter the value of n: "))
        c = int(input("Enter the Cipher Key c: "))
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
            b = pow(a, -1, phi_n)
            for msg in message:
                decrypted.append(pow(int(msg), b, n))
            sys.stdout.write("Message decryption successful\n")
            sys.stdout.write("The decrypted message is: \n")
            message = ''.join(i for i in [chr(x-c) for x in decrypted])
            print(message)
            print(f'Private Key = {b}')
            print(f'Chosen primes = {p1}, {p2}')
    except:
        sys.exit("ERROR: Decryption failed...\nTerminating the program")


if __name__ == '__main__':
    sys.stdout.write("For Encrypting the message Press e/E\n")
    sys.stdout.write("For Decrypting the message Press d/D\n")
    key = input("Press any key to perform action: ").upper()
    if key == 'E':
        encrypt()
    elif key == 'D':
        decrypt()
    else:
        sys.exit("nERROR: Wrong input...\nTerminating the program")


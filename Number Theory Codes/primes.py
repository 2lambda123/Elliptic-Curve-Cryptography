# generates and store the first 15,000,000 prime numbers to a text file
# and uses it to generate keys for RSA Cryto-system
# The 15,000,000th prime is 275,604,541
# NOTE: This program takes a considerable amount of time to generates the 15 million primes
# all the primes have been generated and stored in primes.txt in advance

from math import sqrt, log2


def isprime(N):
    flag = 1
    for i in range(2, int(sqrt(N)) + 1):
        if N % i == 0:
            flag = 0
            break
    else:
        return flag


def generate_primes():
    primes = []
    i = 2
    while len(primes) < 1000000:
        if isprime(i) == 1:
            primes.append(i)
        i += 1
    return primes


primes = generate_primes()

file = open('primes.txt', 'w')
for p in primes[:-1]:
    file.write(str(p) + ', ')
file.write(str(primes[-1]))
file.close()


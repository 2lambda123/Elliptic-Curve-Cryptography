# generates and store the first 15,000,000 prime numbers to a text file
# and uses it to generate keys for RSA Cryto-system
# The 15,000,000th prime is 275,604,541
# NOTE: This program takes a considerable amount of time to generate the 15 million primes
# all the primes have been generated and stored in primes1.txt and primes2.txt in advance
# due to large file size, the primes have been divided into two files

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
    n_primes = []
    i = 2
    while len(primes) + len(n_primes) < 15000000:
        if isprime(i) == 1:
            if len(primes) < 7500000:
                primes.append(i)
            else:
                n_primes.append(i)
        i += 1
    return primes, n_primes


primes, n_primes = generate_primes()

file = open('primes1.txt', 'w')
for p in primes[:-1]:
    file.write(str(p) + ', ')
file.write(str(primes[-1]))
file.close()

file = open('primes2.txt', 'w')
for p in n_primes[:-1]:
    file.write(str(p) + ', ')
file.write(str(n_primes[-1]))
file.close()


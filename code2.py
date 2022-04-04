import math

def isprime(N):
    flag = 1
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            flag = 0
            break
    else:
        return flag

try:
    a, b = input('Elliptic Curve equation coefficients - a, b: ').split()
    p = int(input('Finite Field EC over prime p: '))
    print(f'Elliptic Curve: y^2 = x^3 + {a}x + {b} (mod {p})')
    if isprime(p) != 1:
        print(f'Given number {p} is not a prime number')
        exit()
    x = int(input('x-coordinate on the curve: '))
    a = int(a)
    b = int(b)
    y = x**3 +a*x + b
    y = y % p
    print(f'Point P := ({x}, {y})')
    s = 3*x**2 + a
    s = s / (2*y)
    x2 = (s**2 - 2*x) % p
    y2 = (s*(x - x2) - y) % p
    print(f'Point 2P := ({x2}, {y2})')
except:
    print('Error while computing. Terminating Program')
    exit()


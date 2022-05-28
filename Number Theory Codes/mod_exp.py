# python code for calculating modular exponentiation
# given the values of a, m, n (n in binary)
# calculate a^n mod(n)

def modular_exponentiation(A, N, M):
    binary_n = format(N, "b")
    term = A
    b0 = binary_n[-1]

    if int(b0) == 1:
        answer = A
    else:
        answer = 1

    for b in reversed(binary_n[:-1]):
        term = (term * term) % M
        if int(b) == 1:
            answer = (answer * term) % M
    return answer


def euclidean_algorithm():
    print("Calculating the gcd of any two numbers")
    print("Enter two numbers a, b: ", end="")
    A, B = input().split()
    A = int(a)
    B = int(B)
    while B:
        A, B = B, A % B
    print(f'GCD of given two numbers is {A}')


print("Calculating the value of a^n mod(m)")
a = int(input("Enter the value of a: "))
n = int(input("Enter the value of power(n): "))
m = int(input("Enter the value of modulus(m): "))
value = modular_exponentiation(a, n, m)
print(f'The value of {a}^{n} mod({m}) is {value}')


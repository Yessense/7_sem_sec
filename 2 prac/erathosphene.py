import numpy as np
import random

def get_prime_numbers(n):
    arr = np.ones(n + 1)

    pointer = 2
    while pointer ** 2 < n + 1 :
        if arr[pointer] != 0:
            current_elem = pointer ** 2
            arr[current_elem::pointer] = 0

        pointer += 1
    return arr

def generate_prime_number(n) -> int:
    primes = get_prime_numbers(n)

    while True:
        prime = random.randint(0, n)
        if primes[prime]:
            if prime > 1:
                return prime


if __name__ == '__main__':
    n = int(input())

    prime_numbers = get_prime_numbers(n)
    for i, prime_number in enumerate(prime_numbers):
        if prime_number:
            print(i)




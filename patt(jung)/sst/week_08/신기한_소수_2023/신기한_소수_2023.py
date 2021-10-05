import sys
import math


def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def find_all_primes(n):
    sieve = [False, False] + [True] * (n - 1)
    for i in range(2, n + 1):
        if sieve[i]:
            for j in range(i * 2, n + 1, i):
                sieve[j] = False
    # return primes
    return sieve


def main():
    input1 = sys.stdin.readline
    n = int(input1())
    if n == 1:
        print('2\n3\n5\n7')
        return
    for i in (2, 3, 5, 7):
        loop(n, str(i))


def loop(n, p):
    for i in range(1, 10):
        t = p + str(i)
        if is_prime_number(int(t)):
            if len(t) == n:
                print(t)
            else:
                loop(n, t)


if __name__ == "__main__":
    main()

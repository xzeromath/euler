# https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/
# Instead of checking till n, we can check till √n because a larger factor of n must be a multiple of smaller factor that has been already checked.
# The algorithm can be improved further by observing that all primes are of the form 6k ± 1,
# with the exception of 2 and 3. This is because all integers can be expressed as (6k + i) for some integer k and for i = ?1, 0, 1, 2, 3, or 4;
# 2 divides (6k + 0), (6k + 2), (6k + 4); and 3 divides (6k + 3). So a more efficient method is to test if n is divisible by 2 or 3, then to check through all the numbers of form 6k ± 1. (Source: wikipedia)
# A optimized school method based
# Python3 program to check
# if a number is prime


def isPrime(n):
    # Corner cases
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6

    return True

def prime_list(limit):
    return [i for i in range(limit + 1) if isPrime(i)] #소수 리스트

if __name__ == '__main__':
    limit = 500
    primelist = [i for i in range(limit + 1) if isPrime(i)] #소수 리스트

# This code is contributed
# by Nikita Tiwari.

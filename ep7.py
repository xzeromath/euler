# # 소수를 크기 순으로 나열하면 2, 3, 5, 7, 11, 13, ... 과 같이 됩니다.
# # 이 때 10,001번째의 소수를 구하세요.
# by) 김현기 t
import math

def SOE(n):
     """n 이하의 소수를 나타내는 함수(에라토스테네스의 체), n은 6 이상"""
     a = [False, False] + [True] * (n - 1)
     primes = []
     for i in range(2, n + 1):
        if a[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                a[j] = False
     return primes


def nthprime(n):
    # n번째 소수를 구하는 함수
    m = int(n * (math.log(n) + math.log(math.log(n))))
    primelist = SOE(m)
    return primelist[n - 1]

if __name__ == '__main__':
    print(nthprime(10001))
# 104743

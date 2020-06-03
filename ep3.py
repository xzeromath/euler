# 어떤 수를 소수의 곱으로만 나타내는 것을 소인수분해라 하고, 이 소수들을 그 수의 소인수라고 합니다.

# 예를 들면 13195의 소인수는 5, 7, 13, 29 입니다. 600851475143의 소인수 중에서 가장 큰 수를 구하세요


# 김현기 t
def prime_factorization(n):
    # 자연수 n을 소인수분해
    sol_list= []
    while n % 2 == 0:
        sol_list.append(2)
        n = int(n/2)
    for i in range(3,int(n**0.5)+1,2):
        while n % i == 0:
            sol_list.append(i)
            n = int(n/i)
    if n>2:
        sol_list.append(n)
    return sol_list
print(prime_factorization(600851475143)) #[71, 839, 1471, 6857]
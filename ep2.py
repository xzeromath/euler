# 피보나치 수열의 각 항은 바로 앞의 항 두 개를 더한 것이 됩니다. 1과 2로 시작하는 경우 이 수열은 아래와 같습니다.
#     1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# 짝수이면서 4백만 이하인 모든 항을 더하면 얼마가 됩니까?

def fibo(n):
    """피보나치 수열"""
    a, b = 0, 1
    for i in range(1, n + 1):
        a, b = b, a + b
    return b


mysum2 = 0
i = 1 
while fibo(i) <= 4000000:

    if fibo(i) % 2 == 0:
        mysum2 = mysum2 + fibo(i)
    if fibo(i) > 4000000:
        break
    i = i + 1

print(mysum2)  # 4613732

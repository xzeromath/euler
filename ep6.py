# 1부터 10까지 자연수를 각각 제곱해 더하면 다음과 같습니다 (제곱의 합).
# 12 + 22 + ... + 102 = 385
# 1부터 10을 먼저 더한 다음에 그 결과를 제곱하면 다음과 같습니다 (합의 제곱).
# (1 + 2 + ... + 10)2 = 552 = 3025
# 따라서 1부터 10까지 자연수에 대해 "합의 제곱"과 "제곱의 합" 의 차이는 3025 - 385 = 2640 이 됩니다.
# 그러면 1부터 100까지 자연수에 대해 "합의 제곱"과 "제곱의 합"의 차이는 얼마입니까?
# 조현웅t

n_list = [i for i in range(1,101)]
sqd_list = [j**2 for j in range(1,101)]
print(sum(n_list)**2 - sum(sqd_list))



#김현기 쌤 풀이
def mysum1(n):
    # 합의 제곱 함수 정의
    sum1 = 0
    for i in range(1, n + 1):
        sum1 = sum1 + i
    result1 = sum1 ** 2
    return result1


def mysum2(n):
    # 제곱의 합 함수 정의
    sum2 = 0
    for j in range(1, n + 1):
        sum2 = sum2 + j ** 2
    result2 = sum2
    return result2


print(mysum1(100) - mysum2(100))

#25164150

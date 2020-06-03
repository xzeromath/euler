# 양의 정수 n에 대하여, 다음과 같은 계산 과정을 반복하기로 합니다.
#
#  n → n / 2  (n이 짝수일 때)
# n → 3 n + 1 (n이 홀수일 때)

# 13에 대하여 위의 규칙을 적용해보면 아래처럼 10번의 과정을 통해 1이 됩니다.
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# 아직 증명은 되지 않았지만, 이런 과정을 거치면 어떤 수로 시작해도 마지막에는 1로 끝나리라 생각됩니다.
# (역주: 이것은 콜라츠 추측 Collatz Conjecture이라고 하며, 이런 수들을 우박수 hailstone sequence라 부르기도 합니다)
# 그러면, 백만(1,000,000) 이하의 수로 시작했을 때 1까지 도달하는데 가장 긴 과정을 거치는 숫자는 얼마입니까?
# 참고: 계산 과정 도중에는 숫자가 백만을 넘어가도 괜찮습니다.

# def coll_len(val):
#     """숫자를 받아서 우박수열의 길이 반환"""
#     counter = 0
#     while val != 1:
#         if val % 2 == 0:
#             val = val / 2
#         else:
#             val = 3 * val + 1
#         counter = counter + 1
#     return counter
#
# max_comp = 0
# max_val = 0
# for i in range(1,1000001):
#     result = coll_len(i)
#     if max_val < result:
#         max_comp = i
#         max_val = result
#
# print("가장 긴 수열은 숫자 {}로 시작하는 것이고 그 길이는 {}이다.".format(max_comp,max_val))
# # 가장 긴 수열은 숫자 837799로 시작하는 것이고 그 길이는 524이다.


# 김현기t
def hss(n):
    # n에 대하여 hailstone sequence 과정을 거쳤을 때 그 길이를 계산
    step = 0
    while n!= 1:
        step = step+1
        if n%2 == 0 :
            n = int(n/2)
        else :
            n = 3*n+1
    return step+1

    # step은 계산 횟수를 나타내므로 수열의 길이는 +1

from itertools import count
def hss2(n):
    for i in count(1):
        # print(i)
        if n%2 ==0  :
            n = int(n/2)
        else :
            n = 3*n +1
        if n==1:
            break
    return i
    


def longest_hss(n):
    # n 이하의 수로 시작했을 때 1까지 도달하는데 가장 긴 과정을 거치는 숫자를 구함
    max_comp = 0
    max_val = 0

    for i in range(1,n+1):
        print(i)
        result = hss2(i)
        if max_val< result:
            max_comp = i
            max_val = result
    return max_comp, max_val
print(longest_hss(1000000))

#(837799, 525)
# 2^15 = 32768 의 각 자리수를 더하면 3 + 2 + 7 + 6 + 8 = 26 입니다.
# 2^1000의 각 자리수를 모두 더하면 얼마입니까?
myval = 2**1000
vallist = list(str(myval))
print(sum(list(map(int, vallist))))
# 1366
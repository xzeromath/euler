# 10 이하의 소수를 모두 더하면 2 + 3 + 5 + 7 = 17 이 됩니다.
# 이백만(2,000,000) 이하 소수의 합은 얼마입니까?

from ep7 import SOE

limit = 2000000
# print(SOE(limit))
print(sum(SOE(limit)))

# 142913828922

# n! 이라는 표기법은 n × (n − 1) × ... × 3 × 2 × 1을 뜻합니다. 예를 들자면 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800 이 되는데, 
# 여기서 10!의 각 자리수를 더해 보면 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27 입니다. 100! 의 자리수를 모두 더하면 얼마입니까

# 조현웅t

import math
numstr = str(math.factorial(100))
mylist = [int(i) for i in numstr]
print(sum(mylist))

#648
# 125874를 2배 하면 251748이 되는데, 이 둘은 같은 숫자로 이루어져 있고 순서만 다릅니다.

# 2배, 3배, 4배, 5배, 6배의 결과도 같은 숫자로 이루어지는 가장 작은 수는 무엇입니까?

# 유영주t

import itertools
for i in itertools.count(10**2):
    if set(str(i))==set(str(2*i))== set(str(3*i))== set(str(4*i))== set(str(5*i))== set(str(6*i)):
        print(i)
        break
    else: pass

# 142857
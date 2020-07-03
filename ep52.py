# 125874를 2배 하면 251748이 되는데, 이 둘은 같은 숫자로 이루어져 있고 순서만 다릅니다.

# 2배, 3배, 4배, 5배, 6배의 결과도 같은 숫자로 이루어지는 가장 작은 수는 무엇입니까?

# 유영주t

# import itertools
# for i in itertools.count(10**2):
#     if set(str(i))==set(str(2*i))== set(str(3*i))== set(str(4*i))== set(str(5*i))== set(str(6*i)):
#         print(i)
#         break
#     else: pass

# 142857 중복을 찾지 못함. 

from collections import Counter
import itertools

def dis(val):
    """2x,3x,4x,5x,6x
    가 같은 구성인지 확인"""
    t2 = Counter(list(str(val*2)))
    t3 = Counter(list(str(val*3)))
    t4 = Counter(list(str(val*4)))
    t5 = Counter(list(str(val*5)))
    t6 = Counter(list(str(val*6)))
    return t2 == t3 == t4 == t5 == t6

for i in itertools.count(1):
    if dis(i):
        print(i)
        print(2*i,3*i,4*i,5*i,6*i)
        break
        
# 142857
# 285714 428571 571428 714285 857142
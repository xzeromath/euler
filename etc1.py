# 1년을 365일이라고 하자.
# n명의 사람중에서 같은날, 같은시, 같은분에 태어난 사람의 쌍이 최소한 하나 이상 존재할 확률이 1/2을 넘으려면 최소한 n은 몇 명 있어야 할까요?
# 이 문제를 파이썬으로 해결해봅시다.^^

year_minute = 365*24*60

numOfPeo = 854

import random
result =0


def simu(numOfPeo,mycount):
    result =0
    for j in range(mycount):
        birthday = [random.randint(1,year_minute) for i in range(numOfPeo)]
        if len(set(birthday)) != numOfPeo: # 중복된 사람이 있을 경우
            result = result +1
    return result/mycount

mylist=[]
for i in range(10):
    mylist.append(simu(855,1000))

print(sum(mylist)/len(mylist))

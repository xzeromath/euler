# 소수 중에서 각 자리의 숫자들을 순환시켜도 여전히 소수인 것을 circular prime이라고 합니다.

# 예를 들어 197은 971, 719가 모두 소수이므로 여기에 해당합니다. 이런 소수는 100 밑으로 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97 처럼 13개가 있습니다.

# 그러면 1,000,000 밑으로는 모두 몇 개나 있을까요?

# 조현웅 t

def pr(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
            break
    else:
        return True

result = [2,3,5]
for i in range(6,1000001):
    si = str(i)
    if '0' in si or '2' in si or '4' in si or '5' in si or '6' in si or '8' in si:
        continue
    k = 0
    while pr(i):
        i = int((i-(i%10))/10 + (i%10)*(10**(len(si)-1)))
        k = k + 1
        if k == len(si):
            result.append(i)
            break

print(len(result))
# 55
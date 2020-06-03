
# 1487, 4817, 8147은 3330씩 늘어나는 등차수열입니다. 이 수열에는 특이한 점이 두 가지 있습니다.

# - 세 수는 모두 소수입니다.
# - 세 수는 각각 다른 수의 자릿수를 바꿔서 만들 수 있는 순열(permutation)입니다.

# 1자리, 2자리, 3자리의 소수 중에서는 위와 같은 성질을 갖는 수열이 존재하지 않습니다. 하지만 4자리라면 위엣것 말고도 또 다른 수열이 존재합니다.
# 그 수열의 세 항을 이었을 때 만들어지는 12자리 숫자는 무엇입니까?

def isprime(n):
    # 소수가 맞으면 True, 아니면 False
    if n == 2 or n == 3: 
        return True
    elif n%2 == 0:
        return False
    else:
        for i in range(3,int(n**0.5)+1,2):
            if n%i == 0 :
                return False
    return True

prime_list=[i for i in range(1001,10000,2) if isprime(i)] 
prime_list.sort()

for i in prime_list:
    for j in prime_list:
        if i<j and sorted(list(str(i))) == sorted(list(str(j))):
            k = 2*j - i
            if k in prime_list and sorted(list(str(j))) == sorted(list(str(k))):
                print(i,j,k)
# 1487 4817 8147
# 2969 6299 9629
# 1부터 n까지의 자연수를 차례로 더하여 구해진 값을 삼각수라고 합니다.
# 예를 들어 7번째 삼각수는 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28이 됩니다.
# 이런 식으로 삼각수를 구해 나가면 다음과 같습니다. 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# 이 삼각수들의 약수를 구해봅시다.  
# 1: 1  3: 1, 3  6: 1, 2, 3, 6 10: 1, 2, 5, 10 15: 1, 3, 5, 15 21: 1, 3, 7, 21 28: 1, 2, 4, 7, 14, 28
# 위에서 보듯이, 5개 이상의 약수를 갖는 첫번째 삼각수는 28입니다. 그러면 500개 이상의 약수를 갖는 가장 작은 삼각수는 얼마입니까? 

def triangle_number(n):
    #n번째 삼각수
    return sum(list(range(1,n+1)))

def divisor_length(n):
    # n의 약수의 개수 반환
    my_list=[]
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            my_list.append(i)
            my_list.append(n/i)
    return len(set(my_list))

# 약수의 개수가 500이상이 되는 최소의 삼각수
i=0
m=1
while divisor_length(m) < 500:
    i +=1
    m=triangle_number(i)
    
print(m,i+1,divisor_length(m)) 
# 76576500 12375 576


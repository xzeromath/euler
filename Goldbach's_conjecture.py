#     2보다 큰 모든 짝수는 두 소수의 합으로 표현가능하다.
# 골드바흐의 추측에서 다음을 해결해봅시다.
# 2초과 500이하의 짝수를 두 소수의 합으로 모두 표현하시오.

from myprimes import isPrime, prime_list


def prime_sum(mynum):
    mylist = prime_list(mynum)
    for i in mylist:
        if mynum - i in mylist:
            return i, mynum -i
print(prime_sum(600))

for i in range(4,5001,2):
    print("{}={}+{}".format(i,*prime_sum(i)))
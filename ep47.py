#  [EP47-상] 서로 다른 네 개의 소인수를 갖는 수들이 처음으로 네 번 연속되는 경우는? 

# from myfunctions import isPrime
# import itertools

# def factorlist(value):
#     """value를 입력받아 소인수가 네개이면 true"""
#     my_list=[]
#     i=2
#     while not isPrime(value):

#         if value % i ==0 and isPrime(i):
#             my_list.append(i)
#             value = value // i
#             i =2

#         else:
#             i=i+1
#     my_list.append(value)

#     return len(set(my_list))==4


# print(factorlist(207))
# for i in itertools.count(2):
#     if all([factorlist(i),factorlist(i+1),factorlist(i+2),factorlist(i+3)]):
#         print(i,i+1,i+2,i+3)
#         break
    
# 134043 134044 134045 134046

# 김현기t : 좀더 빠름.
def pr_fac(n):
    """자연수 n을 소인수분해"""
    sol_list= []
    while n % 2 == 0:
        sol_list.append(2)
        n = int(n/2)
    for i in range(3,int(n**0.5)+1,2):
        while n % i == 0:
            sol_list.append(i)
            n = int(n/i)
    if n>2:
        sol_list.append(n)
    return sorted(sol_list)


def is_pr4_fac(n):
    """n이 서로 다른 네 개의 소인수를 가짐"""
    if len(set(pr_fac(n))) == 4:
        return True
    else:
        return False
    
p = 2*3*5*7
sol = 0
while sol == 0:
    i=0
    while is_pr4_fac(p+i) and is_pr4_fac(p+1+i):
        i +=1
        if i == 3:
            sol = p
            break
    p += 1  
    
print(sol,sol+1,sol+2,sol+3)
    
# 134043 134044 134045 134046
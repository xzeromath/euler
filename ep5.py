# 1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.
# 그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?

#방법 1 : 오래 걸림
# value = 1
# check = True
# while check:
#     for i in range(1,21):
#         print()
#         if value % i == 0 :
#             continue
#         else :
#             value = value+1
#             break

#         print("kk",value)
#     else:
#         print(value)
#         break


# 방법2: 수학이론을 적용한 더 빠르고 좋은 방법 #김웅규 t

def gcd(a,b):
    while (b!=0):
        r=a%b
        a,b=b,r
    return a
def lcm(a,b):
    return a*b/gcd(a,b)

n=20
c=lcm(1,2)
for i in range(3,n+1):
    c=lcm(c,i)
print(c)


#232792560.0
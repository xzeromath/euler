# 세 변의 길이가 모두 자연수 {a, b, c}인 직각삼각형의 둘레를 p 로 둘 때, p = 120 을 만족하는 직각삼각형은 아래와 같이 세 개가 있습니다.
# {20, 48, 52}, {24, 45, 51}, {30, 40, 50}
# 1000 이하의 둘레 p에 대해서, 직각삼각형이 가장 많이 만들어지는 p의 값은 얼마입니까?

# 노창균t

def myn(n):
    my_lenth =0
    my_list =[]
    for x in range(1,(n//3) +1):
        for y in range((n-3*x)//2 +1):
            z = n-3*x -2*y
            a,b,c= x, x+y, x+y+z
            if a**2 +b**2 ==c **2:
                my_list.append((a,b,c))
                my_lenth += 1
    return my_lenth, my_list

max_length , max_list, max_i =0,[],0
for i in range(1,1001):
    result = myn(i)
    if result[0] >max_length:
        max_length = result[0]
        max_list = result[1]
        max_i =i

print("가장 큰 수는 {}이고 순서쌍의 수는 {} 이고, 이 리스트는 {}이다".format(max_i,max_length, max_list))

# 가장 큰 수는 1000이고 순서쌍의 수는 8 이고,
# 이 리스트는 [(40, 399, 401), (56, 390, 394), (105, 360, 375), (120, 350, 370), (140, 336, 364), (168, 315, 357), (210, 280, 350), (240, 252, 348)]이다


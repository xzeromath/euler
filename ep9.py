# 세 자연수 a, b, c 가
#  피타고라스 정리  a2 + b2 = c2 를 만족하면 피타고라스 수라고 부릅니다
# (여기서  a < b < c ).
# 예를 들면 32 + 42 = 9 + 16 = 25 = 52이므로 3, 4, 5는 피타고라스 수입니다.
#   a + b + c = 1000  인 피타고라스 수
#  a, b, c는 한 가지 뿐입니다.
#  이 때,  a × b × c 는 얼마입니까?

for i in range(1,1000):
    for j in range(i+1,1000-i):
        k = 1000 - i -j
        if k**2 == i**2 + j**2:
            print("세 수는 {},{},{}이다. ".format(i,j,k))
            print("곱은 {}이다.".format(i*j*k))

# 세 수는 200,375,425이다.
# 곱은 31875000이다.
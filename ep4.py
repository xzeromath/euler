# 앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를
# 대칭수(palindrome)라고 부릅니다. 두 자리 수를 곱해 만들 수 있는
# 대칭수 중 가장 큰 수는 9009 (= 91 × 99) 입니다. 세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수는 얼마입니까?

result, a, b = 0, 0, 0

for i in range(100, 1000):
    for j in range(100, 1000):
        k = str(i * j)
        reverse_k = k[::-1]
        if k == reverse_k and result < int(k):
            result = int(k)
            a, b = i, j

print("가장 큰 수는 {}이다.".format(result))
print("두 수는 {},{}이다. ".format(a, b))

# 가장 큰 수는 906609이다.
# 두 수는 913,993이다.

# 분자가 1인 분수를 단위분수라고 합니다.
# 분모가 2에서 10까지의 단위분수는 아래와 같습니다.
# 숫자 위에 찍힌 점은 순환마디를 나타내는데, 1/6의 경우 순환마디는 "6"으로 0.166666...처럼 6이 무한히 반복됨을 뜻합니다.
# 같은 식으로 1/7은 6자리의 순환마디(142857)를 가집니다.
# d 를 1000 이하의 정수라고 할 때, 단위분수 1/d 의 순환마디가 가장 긴 수는 무엇입니까?

# 1-> 10 -> 나머지 3 -> 30 -> 나머지2 -> 20 -> 나머지6 ...

# 김현기, 노창균 t

def denofun(Deno):
    """ 분모를 입력받아 1/분모의 순환마디 길이 출력"""
    result, result_list = 1, []
    for i in range(Deno):  # 순환마디의 길이는 최대 Deno까지
        result = result * 10 % Deno
        if result == 0:  # 유한소수일 경우
            return -1
        elif result in result_list:  # 순환마디가 결정된 경우
            return len(result_list[result_list.index(result):])

        else:
            result_list.append(result)


max_length, max_com = 0, 0
for i in range(1, 1001):
    re = denofun(i)
    if max_length < re:
        max_length = re
        max_com = i

print("순환마디가 가장 큰 수는 1/{}이며 길이는 {}이다".format(max_com, max_length))

# 순환마디가 가장 큰 수는 1/983이며 길이는 982이다

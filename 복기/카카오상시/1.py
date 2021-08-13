# - 1. 한번만 사용한 첫 문자 찾기
# - 문자열에서 한번만 사용한 문자를 찾고자 함. 문자열은 소문자만 사용함
# - 한번만 사용한 문자 중 먼저 나타난 문자의 인덱스를 리턴해야 함.
# - 인덱스는 1부터 시작함. 한번만 사용한 문자가 없을 경우 -1을 리턴해야 함.
# - ex) s = "statistics"
# - -> [a, c]

s = "statistics"
s1 = "ssssaaabcd"
s2 = "dffasdfasdfsa"


def sol(str):  # 파이썬 dic - 내부적으로 순서 유지

    dic = {}
    res = []
    for c in str:
        dic[c] = dic.get(c, 0)+1
    for key in dic.keys():
        if dic[key] == 1:
            res.append(key)
    if res:
        return res
    else:
        return -1


print(sol(s))
print(sol(s1))
print(sol(s2))

import itertools as it

# 잘못된 풀이 -> TLE
# 접근자체는 맞았으나 옷의 종류가 매우 많을 경우 무조건 TLE다


def solution(clothes):
    dic = {}

    for c in clothes:
        dic[c[1]] = dic.get(c[1], [])
    for c in clothes:
        dic[c[1]].append(c[0])

    arr = []
    for d in dic.values():
        arr.append(len(d))
    res = 0
    for i in range(1, len(arr)+1):
        for tmp in it.combinations(arr, i):
            s = 1
            for t in tmp:
                s *= t
            res += s
    return res

# 조합 사용하지 않고 간단한 수학적 계산으로 푸는 방법
# 입는 경우와 입지 않는 경우를 따져서 곱해줘야함.
# 마지막엔 전부다 입지 않는 경우를 생각하여야함


def solution2(clothes):
    dic = {}
    for c in clothes:
        dic[c[1]] = dic.get(c[1], [])
    for c in clothes:
        dic[c[1]].append(c[0])
    res = 1
    for d in dic.values():
        res *= (len(d)+1)
    return res-1

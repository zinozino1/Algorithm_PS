# 1번 의류구매
# 해시+구현 문제
# 상의와 하의의 딕셔너리를 따로 만들어야한다. 시험장에선 하나의 딕셔너리로 했다가 손 꼬임


def solution(color, prices):
    top = {}
    bottom = {}

    for c in color:
        top[c[0]] = top.get(c[0], 0) + 1
        bottom[c[1]] = bottom.get(c[1], 0) + 1

    res = 0
    for t in top.keys():
        if bottom.get(t):
            tmp = min(top[t], bottom[t])
            res += prices[0] * tmp
            top[t] -= tmp
            bottom[t] -= tmp

    tot_cnt = 0
    for t in top.keys():
        if top[t] != 0:
            tot_cnt += top[t]

    for b in bottom.keys():
        if bottom[b] != 0:
            tot_cnt += bottom[b]

    res += min(tot_cnt * prices[0], int(tot_cnt/2+0.5) * prices[1])

    return res


print(solution(["RG", "WR", "BW", "GG"], [5000, 6000]))
print(solution(["RG", "WR", "BW", "GG"], [2000, 6000]))
print(solution(["BW", "RY", "BY"], [9000, 10000]))
print(solution(["YW", "RY", "WG", "BW"], [7561, 8945]))

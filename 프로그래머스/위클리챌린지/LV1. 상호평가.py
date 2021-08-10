# 단순 구현

def solution(scores):
    n = len(scores)
    res = []
    for i in range(n):
        maxN, minN = -1e9, 1e9
        for j in range(n):
            maxN = max(maxN, scores[j][i])
            minN = min(minN, scores[j][i])
        maxCnt, minCnt = 0, 0
        for j in range(n):
            if scores[j][i] == maxN:
                maxCnt += 1
            if scores[j][i] == minN:
                minCnt += 1

        for j in range(n):
            if i == j:
                if maxCnt == 1 and scores[j][i] == maxN:
                    scores[j][i] = 0
                if minCnt == 1 and scores[j][i] == minN:
                    scores[j][i] = 0
        s = 0
        cnt = 0
        for j in range(n):
            if scores[j][i] != 0:
                cnt += 1
                s += scores[j][i]
        if cnt != 0:
            s /= cnt
        else:
            s = 0
        res.append(s)
    final = ''

    for r in res:
        if r >= 90:
            final += "A"
        elif 80 <= r < 90:
            final += "B"
        elif 70 <= r < 80:
            final += "C"
        elif 50 <= r < 70:
            final += "D"
        else:
            final += "F"

    return final

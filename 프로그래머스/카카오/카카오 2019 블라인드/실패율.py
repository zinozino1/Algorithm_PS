# 구현
# 30분

def solution(N, stages):
    person = {}

    for i in range(1, N+1):
        person[i] = 1
    for s in stages:
        if person.get(s):
            person[s] += 1

    tot = 0
    res = []
    for key in person.keys():
        if (len(stages) - tot) != 0:
            res.append((key, (person[key] - 1) / (len(stages) - tot)))
        else:
            res.append((key, 0))
        tot += person[key]-1

    res.sort(key=lambda x: (-x[1], x[0]))

    return [stage for stage, rate in res]

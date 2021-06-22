def solution(d, budget):
    d.sort()
    acc = 0
    cnt = 0
    for i in range(len(d)):
        acc += d[i]
        if acc > budget:
            break
        cnt += 1
    return cnt

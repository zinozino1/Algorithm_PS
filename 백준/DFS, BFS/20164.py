# 골드5 - 홀수 홀릭 호석
# DFS

n = int(input())
curr = str(n)
maxLen = -1e9
minLen = 1e9
odd_cnt = 0
for s in curr:
    if int(s) % 2 == 1:
        odd_cnt += 1

maxCnt = -1e9
minCnt = 1e9


def dfs(target, tot):

    global maxCnt, minCnt

    if len(target) == 1:
        maxCnt = max(maxCnt, tot)
        minCnt = min(minCnt, tot)
        return

    else:
        if len(target) == 2:
            next_target = str(int(target[0]) + int(target[1]))
            if len(next_target) == 2:
                next_odd_cnt = 0
                if int(next_target[0]) % 2 == 1:
                    next_odd_cnt += 1
                if int(next_target[1]) % 2 == 1:
                    next_odd_cnt += 1
                dfs(next_target, tot+next_odd_cnt)
            else:
                if int(next_target) % 2 == 1:
                    dfs(next_target, tot+1)
                else:
                    dfs(next_target, tot)

        elif len(target) > 2:
            for lt in range(1, len(target) - 1):
                for rt in range(lt + 1, len(target)):
                    first = target[:lt]
                    second = target[lt:rt]
                    third = target[rt:]

                    next_target = str(int(first) + int(second) + int(third))
                    next_odd_cnt = 0
                    for k in next_target:
                        if int(k) % 2 == 1:
                            next_odd_cnt += 1
                    dfs(next_target, tot + next_odd_cnt)


dfs(curr, odd_cnt)

print(minCnt, maxCnt)

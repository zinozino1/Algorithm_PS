# 골드4-가르침-문자열
# 해시로 풀려했으나 절대 안풀림
# DFS로 모든 경우 탐색하는데 모든 경우의 수가 26C10이므로 무조건 시간초과
# 따라서 모든 알파벳이 아니라 있는 알파벳만 가르침

import sys

input = sys.stdin.readline


def sol():
    global max_cnt
    max_cnt = 0
    n, k = map(int, input().split())
    targets = [input().strip() for _ in range(n)]
    remove_set = ["a", "c", "t", "i", "n"]
    for i in range(len(targets)):
        for j in range(5):
            if remove_set[j] in targets[i]:
                targets[i] = list(targets[i].replace(remove_set[j], ""))
                targets[i].sort()
                targets[i] = "".join(targets[i])
                if targets[i] == "":
                    max_cnt += 1

    s = set()
    for i in range(n):
        for j in range(len(targets[i])):
            s.add(targets[i][j])
    tmp = []+list(s)

    def dfs(L, s, tot):
        global max_cnt

        if len(tot) > k-5:
            return
        if L == k-5:
            cnt = 0

            for q in range(n):
                flag = True
                for p in range(len(targets[q])):
                    if targets[q][p] not in tot:
                        flag = False
                        break
                if flag:
                    cnt += 1

            if cnt > max_cnt:
                max_cnt = cnt
            return
        else:
            for i in range(s, len(tmp)):
                dfs(L+1, i+1, tot+tmp[i])

    if k-5 < 0:
        print(0)
    else:
        dfs(0, 0, '')
        print(max_cnt)


sol()

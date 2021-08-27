# 실버1 - 징검다리 건너기
# BFS or dp

from collections import deque


n = int(input())
jumps = [tuple(map(int, input().split())) for _ in range(n-1)]
k = int(input())

min_enegy = 1e9


def bfs():
    global min_enegy
    q = deque()
    q.append((0, 1, 0))  # (현재 돌, 큰점프 남은 횟수, value)
    check = set()
    check.add((0, 1, 0))
    while q:

        for _ in range(len(q)):
            curr_stone, big, value = q.popleft()
            if curr_stone == n-1:
                min_enegy = min(min_enegy, value)
            for s in range(3):
                if s == 0:  # 작은 점프
                    if curr_stone + 1 <= n-1 and (curr_stone + 1, big, value + jumps[curr_stone][0]) not in check:
                        check.add(
                            (curr_stone + 1, big, value + jumps[curr_stone][0]))
                        q.append(
                            (curr_stone + 1, big, value + jumps[curr_stone][0]))
                elif s == 1:  # 큰 점프
                    if curr_stone + 2 <= n-1 and (curr_stone + 2, big, value + jumps[curr_stone][1]) not in check:
                        check.add(
                            (curr_stone + 2, big, value + jumps[curr_stone][1]))
                        q.append(
                            (curr_stone + 2, big, value + jumps[curr_stone][1]))
                else:  # 매우 큰 점프
                    if curr_stone + 3 <= n-1 and (curr_stone + 3, big, value + k) not in check and big == 1:
                        check.add((curr_stone + 3, big-1, value + k))
                        q.append((curr_stone + 3, big-1, value + k))


bfs()

print(min_enegy)


# dp 풀이


n = int(input())
jumps = [tuple(map(int, input().split())) for _ in range(n-1)]
k = int(input())

dp = [1e9]*n
dp[0] = 0

for dis in range(1, 4):
    if dis == 1:
        for i in range(dis, n):
            dp[i] = min(dp[i], dp[i-dis]+jumps[i-dis][0])
    elif dis == 2:
        for i in range(dis, n):
            dp[i] = min(dp[i], dp[i-dis]+jumps[i-dis][1])
    else:
        for i in range(dis, n):
            dp[i] = min(dp[i], dp[i-dis]+k)

print(dp[n-1])

# 골드5 - DSLR
# BFS

# 단순 BFS. 중복 체크 시간을 얼마나 줄이느냐가 관건이었다
# BFS 풀 때 set 말고 이차원 배열이나 일차원 체크 배열을 고민해볼것

from collections import deque


T = int(input())


def num_to_str(num):
    tmp = str(num)
    return "0"*(4-len(tmp))+tmp


def bfs(R):
    q = deque()
    q.append((R, ''))
    level = 0
    while q:
        for _ in range(len(q)):
            v, c = q.popleft()
            for s in range(4):
                # D
                if s == 0:
                    double = 2*v
                    if double > 9999:
                        if check[double % 10000] == 0:
                            check[double % 10000] = 1
                            q.append((double % 10000, c+"D"))
                        if double % 10000 == B:
                            return c+"D"
                    else:
                        if check[double] == 0:
                            check[double] = 1
                            q.append((double, c+"D"))
                        if double == B:
                            return c+"D"
                # S
                elif s == 1:
                    sub = v-1
                    if v == 0:
                        if check[9999] == 0:
                            check[9999] = 1
                            q.append((9999, c+"S"))
                        if 9999 == B:
                            return c+"S"
                    else:
                        if check[sub] == 0:
                            check[sub] = 1
                            q.append((sub, c+"S"))
                        if sub == B:
                            return c+"S"
                # L
                elif s == 2:
                    left = num_to_str(v)[1:]+num_to_str(v)[0]
                    if check[int(left)] == 0:
                        check[int(left)] = 1
                        q.append((int(left), c+"L"))
                    if int(left) == B:
                        return c+"L"
                # R
                elif s == 3:
                    right = num_to_str(v)[-1]+num_to_str(v)[:-1]
                    if check[int(right)] == 0:
                        check[int(right)] = 1
                        q.append((int(right), c+"R"))
                    if int(right) == B:
                        return c+"R"
        level += 1


for _ in range(T):
    A, B = map(int, input().split())
    check = [0]*10001
    res = ''
    print(bfs(A))

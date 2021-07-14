# 13:03 - 13:55
# 골드5-스타트링크
# 무난한 BFS였으나 출력값 삽질로 인해 시간 낭비

from collections import deque

f, s, g, u, d = map(int, input().split())

check = set()  # 방문한 경로는 가지 않는다 -> 체크배열로 최적화 가능할듯


def bfs():
    q = deque()
    q.append(s)
    cnt = 0
    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            for next in [curr+u, curr-d]:
                if next == g:
                    return cnt
                elif next > 0 and next <= f:
                    if next not in check:
                        check.add(next)
                        q.append(next)
        cnt += 1


if s == g:
    print(0)
else:
    res = bfs()
    if res == None:
        print("use the stairs")
    else:
        print(res+1)

# 최적화 풀이


# f, s, g, u, d = map(int, input().split())

# check = [0]*(f+1)


# def bfs2():
#     q = deque()
#     q.append(s)
#     cnt = 0
#     while q:
#         for _ in range(len(q)):
#             curr = q.popleft()
#             for next in [curr+u, curr-d]:
#                 if next == g:
#                     return cnt
#                 elif next > 0 and next <= f:
#                     if check[next] == 0:
#                         check[next] = 1
#                         q.append(next)
#         cnt += 1


# if s == g:
#     print(0)
# else:
#     res = bfs2()
#     if res == None:
#         print("use the stairs")
#     else:
#         print(res+1)

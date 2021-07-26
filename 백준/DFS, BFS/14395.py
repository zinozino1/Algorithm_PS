# 골드5 - 4연산
# BFS

# 무난한 BFS 문제. 연산자의 순서가 정해져있으므로 미리 oper배열을 정해놓으면
# 굳이 결과들을 다 담을 필요 없이 바로 리턴하면 된다.

from collections import deque

s, t = map(int, input().split())
check = set()
oper = ["*", "+", "-", "/"]


def bfs():
    q = deque()
    q.append([s, ""])
    check.add(s)
    while q:
        for _ in range(len(q)):
            curr, seq = q.popleft()
            # 검사
            if curr == t:
                return seq
            if curr == 0:
                continue
            # 루프 -> 연산량 줄이기 위해 eval사용 x
            for k in range(4):
                next = curr
                if k == 0:
                    next = curr * curr
                elif k == 1:
                    next = curr + curr
                elif k == 2:
                    next = curr - curr
                else:
                    next = curr // curr
                if next > 10e9:
                    continue
                # 타겟 방문 중복 체크는 안해야되는줄 알았으나 어차피 연산자의 순서는 정해져있으므로 이 코드는 필요 없다.
                if next == t:
                    q.append([next, seq+oper[k]])
                elif next not in check:
                    check.add(next)
                    q.append([next, seq+oper[k]])
    return -1


if s == t:
    print(0)
else:
    print(bfs())

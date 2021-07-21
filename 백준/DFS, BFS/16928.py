# 실버1 - 뱀과사다리게임
# BFS
# 아니 이 코드가 대체 왜 틀린건지 모르겠다 ㅅㅂ


from collections import deque

n, m = map(int, input().split())

dic = {}

for _ in range(n):
    s, e = map(int, input().split())
    dic[s] = e
for _ in range(m):
    s, e = map(int, input().split())
    dic[s] = e
check = set()
check.add(1)


def bfs(v):
    q = deque()
    q.append((v, 0))
    level = 0
    while q:
        for _ in range(len(q)):
            nv, cnt = q.popleft()

            # 포탈
            if dic.get(nv):
                if dic.get(nv) not in check:
                    check.add(dic.get(nv))
                    q.append((dic.get(nv), cnt))
                    if nv == 100:
                        return cnt

            # 주사위 던지기
            else:
                for s in range(1, 7):
                    if not nv+s in check and 1 <= nv+s <= 100:
                        check.add(nv+s)
                        q.append((nv+s, cnt+1))
                        if nv+s == 100:
                            return cnt + 1
        level += 1


print(bfs(1))

# 실버1 - 물통
# DFS

# 현대카트 3번과 유사하나 이게 더 어려움
# 사람들은 BFS로 풀던데 난 DFS로 풀음


a, b, c = map(int, input().split())
check = set()
check.add((0, 0, c))


def dfs(A, B, C):
    for s in range(6):
        if s == 0:
            # a->b
            NA, NB, NC = A, B, C
            if NB+NA > b:
                NA = NA-(b-NB)
                NB = b
            else:
                NB = NB+NA
                NA = 0

            if (NA, NB, NC) not in check:
                check.add((NA, NB, NC))
                dfs(NA, NB, NC)
        # a->c
        elif s == 1:
            NA, NB, NC = A, B, C
            if NC+NA > c:
                NA = NA-(c-NC)
                NC = c
            else:
                NC = NC+NA
                NA = 0

            if (NA, NB, NC) not in check:
                check.add((NA, NB, NC))
                dfs(NA, NB, NC)
        # b->a
        elif s == 2:
            NA, NB, NC = A, B, C
            if NA+NB > a:
                NB = NB-(a-NA)
                NA = a
            else:
                NA = A+B
                NB = 0

            if (NA, NB, NC) not in check:
                check.add((NA, NB, NC))
                dfs(NA, NB, NC)
        # b->c
        elif s == 3:
            NA, NB, NC = A, B, C
            if NC+NB > c:
                NB = NB-(c-NC)
                NC = c
            else:
                NC = NC+NB
                NB = 0

            if (NA, NB, NC) not in check:
                check.add((NA, NB, NC))
                dfs(NA, NB, NC)
        # c->a
        elif s == 4:
            NA, NB, NC = A, B, C
            if NA+NC > a:
                NC = NC-(a-NA)
                NA = a
            else:
                NA = NA+NC
                NC = 0

            if (NA, NB, NC) not in check:
                check.add((NA, NB, NC))
                dfs(NA, NB, NC)
        # c->b
        elif s == 5:
            NA, NB, NC = A, B, C
            if NB+NC > b:
                NC = NC-(b-NB)
                NB = b
            else:
                NB = NB+NC
                NC = 0

            if (NA, NB, NC) not in check:
                check.add((NA, NB, NC))
                dfs(NA, NB, NC)


dfs(0, 0, c)

res = set()
for c in check:
    if c[0] == 0:
        res.add(c[2])

print(*sorted(list(res)))

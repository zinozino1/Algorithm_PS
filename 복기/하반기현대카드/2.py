# 2번 자연수와 m
# dfs 순열문제

# 최대 9!까지이므로 백트래킹 안해도 된다
# 백트래킹 할 것도 없음

def solution(k, m):
    global cnt
    check = [0] * (k+1)
    cnt = 0

    def dfs(L, n, tot):
        global cnt
        if L == n:
            if int(tot) % m == 0:
                cnt += 1
            return
        else:
            for i in range(1, n + 1):
                if check[i] == 0:
                    check[i] = 1
                    dfs(L+1, n, tot+str(i))
                    check[i] = 0

    dfs(0, k, '')
    return cnt


print(solution(3, 2))
print(solution(4, 77))
print(solution(5, 1))
print(solution(9, 31233))

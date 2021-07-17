# 실버1-연산자끼워넣기
# DFS

# 풀긴 풀었는데 코드가 굉장히 더럽네
# eval쓰면 TLE

import sys
import itertools as it

n = int(input())
target = list(map(int, input().split()))
oper_cnt = list(map(int, input().split()))
oper_dic = {}

for i, o in enumerate(oper_cnt):
    if i == 0 and o != 0:
        oper_dic["+"] = oper_dic.get("+", 0) + o
    elif i == 1 and o != 0:
        oper_dic["-"] = oper_dic.get("-", 0) + o
    elif i == 2 and o != 0:
        oper_dic["*"] = oper_dic.get("*", 0) + o
    elif i == 3 and o != 0:
        oper_dic["//"] = oper_dic.get("//", 0) + o
oper_arr = []
for tmp in oper_dic.keys():
    for i in range(oper_dic[tmp]):
        oper_arr.append(tmp)

max_n = -sys.maxsize
min_n = sys.maxsize

for tmp in it.permutations(oper_arr):
    acc = target[0]

    for i in range(1, len(target)):
        if tmp[i-1] == "//":
            if acc < 0:
                acc = -(-acc // target[i])
            else:
                acc //= target[i]
        elif tmp[i-1] == "+":
            acc += target[i]
        elif tmp[i-1] == "-":
            acc -= target[i]
        elif tmp[i-1] == "*":
            acc *= target[i]
        # else:
        #   acc = eval(str(acc)+tmp[i-1]+str(target[i]))

    if acc > max_n:
        max_n = acc
    if acc < min_n:
        min_n = acc

print(max_n)
print(min_n)


# 고수 풀이
# 상태트리가 모든 연산자의 모임이 아닌 +,-,*,/ 이렇게 4가지로 계속 뻗음
# 뻗다가 각 연산자의 카운트가 0이되면 백트래킹

# 모든 연산자의 모임으로 해도 되긴 하지만 이 코드가 훨씬 간결하다 .

n = int(input())
target = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
max_n = -sys.maxsize
min_n = sys.maxsize


def dfs(L, tot):
    global add, sub, mul, div, max_n, min_n
    if L == n-1:

        if tot > max_n:
            max_n = tot
        if tot < min_n:
            min_n = tot
        return
    else:
        if add > 0:
            add -= 1
            dfs(L+1, tot+target[L+1])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(L+1, tot-target[L+1])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(L+1, tot*target[L+1])
            mul += 1
        if div > 0:
            div -= 1
            dfs(L+1, int(tot/target[L+1]))
            div += 1


dfs(0, target[0])
print(max_n)
print(min_n)

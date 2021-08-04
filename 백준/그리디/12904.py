# 골드5 - A와B
# 그리디
# S->T가 아니라 T->S로 생각하면 쉽게 풀리는 문제

S = input().strip()
T = input().strip()

while S != T:
    if len(S) > len(T):
        break
    if T[-1] == "B":
        T = T[:len(T)-1]
        T = T[::-1]
    elif T[-1] == "A":
        T = T[:len(T)-1]

if S == T:
    print(1)
else:
    print(0)

# 골드4 - 내려가기
# dp

# 메모리를 쓰지 않기 위해 추가배열을 사용해주는데
# ex) maxdp[0] => 계산의 대상 maxdp[1] -> 계산의 결과 임시저장

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
maxdp = [[arr[0][0], arr[0][1], arr[0][2]], [arr[0][0], arr[0][1], arr[0][2]]]
mindp = [[arr[0][0], arr[0][1], arr[0][2]], [arr[0][0], arr[0][1], arr[0][2]]]

for i in range(1, n):
    for j in range(3):
        if j == 0:
            maxdp[1][j] = max(maxdp[0][0], maxdp[0][1]) + arr[i][j]
            mindp[1][j] = min(mindp[0][0], mindp[0][1]) + arr[i][j]
        elif j == 1:
            maxdp[1][j] = max(maxdp[0][0], maxdp[0][1],
                              maxdp[0][2]) + arr[i][j]
            mindp[1][j] = min(mindp[0][0], mindp[0][1],
                              mindp[0][2]) + arr[i][j]
        elif j == 2:
            maxdp[1][j] = max(maxdp[0][1], maxdp[0][2]) + arr[i][j]
            mindp[1][j] = min(mindp[0][1], mindp[0][2]) + arr[i][j]
    for j in range(3):
        maxdp[0][j] = maxdp[1][j]
        mindp[0][j] = mindp[1][j]

print(max(maxdp[1]), min(mindp[1]))

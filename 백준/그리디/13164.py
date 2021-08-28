# 골드5 - 행복 유치원
# 그리디

# 처음에 이분탐색으로 접근했다가 helper 로직을 구현하기가 어려워서 포기
# 작은 문제로 해결할 수 없을 것 같아 dp도 포기
# 그리디로 풀어야함
# 인접한 값의 차이로 구성된 배열을 만들고 그것을 오름차순 정렬
# n-k 개수만큼 더해주면 답


n, k = map(int, input().split())
arr = list(map(int, input().split()))
dis = []
for i in range(1, n):
    dis.append(arr[i]-arr[i-1])
dis.sort()
res = sum(dis[i] for i in range(n-k))
print(res)

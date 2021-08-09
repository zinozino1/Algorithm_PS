# 실버3 - 수열
# 슬라이딩 윈도우

# 처음에 k가 없는줄 알고 삽질함
# 정해진 k가 있으면 쉬운 문제
# 윈도우를 한 칸씩 이동시키면서 res를 업데이트시키면 된다.

n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 윈도우 사이즈 정의
lt = 0
rt = k
s = sum(arr[:k])
res = s
while lt <= n-k-1:
    s = s-arr[lt]+arr[rt]
    res = max(res, s)
    # 윈도우 이동
    lt += 1
    rt += 1
print(res)

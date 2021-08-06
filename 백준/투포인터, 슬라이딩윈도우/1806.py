# 골드4 - 부분합
# 투포인터

# 투포인터 아직 미숙


import sys
n, s = map(int, input().split())
seq = list(map(int, input().split()))
maxN = max(seq)

if maxN >= s:
    print(1)
else:
    lt = 0
    rt = 1
    tot = seq[lt]+seq[rt]
    res = 1e9
    cnt = 2
    while lt <= n-1 and rt <= n-1:
        if tot < s:
            rt += 1
            cnt += 1
            if rt <= n-1:
                tot += seq[rt]
        else:  # 만족
            res = min(cnt, res)
            tot -= seq[lt]
            lt += 1
            cnt -= 1

    if tot >= s and res > cnt:
        res = cnt
    if res == 1e9:
        print(0)
    else:
        print(res)


# 개선된 풀이 - 기본적인 접근법은 동일하나 코드 품질의 차이

N, S = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
tmp_sum = 0
min_length = sys.maxsize

while True:
    if tmp_sum >= S:
        min_length = min(min_length, right - left)
        tmp_sum -= arr[left]
        left += 1

    elif right == N:
        break

    else:
        tmp_sum += arr[right]
        right += 1

if min_length == sys.maxsize:
    print(0)
else:
    print(min_length)

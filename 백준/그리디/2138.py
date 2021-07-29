# 실버2 - 전구와 스위치
# 그리디

# 첫번째 스위치를 켜는 경우와 키지 않는 경우로 분기해야함


n = int(input())
c = list(map(int, input().rstrip("\n")))
want = list(map(int, input().rstrip("\n")))


def change(num):
    if num == 0:
        num = 1
    else:
        num = 0
    return num


def switch(c, cnt):
    count = cnt
    if count == 1:  # 첫번째 스위치 누른 경우
        c[0] = change(c[0])
        c[1] = change(c[1])
    for i in range(1, n):
        # 이전 전구의 값을 비교함
        if c[i - 1] != want[i - 1]:
            count += 1
            c[i - 1] = change(c[i - 1])
            c[i] = change(c[i])
            if i != n - 1:
                c[i + 1] = change(c[i + 1])
    if c == want:
        return count
    else:
        return -1


res1 = switch(c[:], 0)  # 시작점 스위치를 누르지 않는 경우
res2 = switch(c[:], 1)  # 시작점 스위치를 누르는 경우
if res1 >= 0 and res2 >= 0:
    print(min(res1, res2))
elif res1 >= 0 and res2 < 0:
    print(res1)
elif res1 < 0 and res2 >= 0:
    print(res2)
else:
    print(-1)

# 그리디로 푸는 것이 맞는가부터 파악
# 가장 큰 수인 5로 나누면 되나 11 같은 수는 5+3+3이므로 중간에서 걸러줘야함
# 그리디를 가장한 탐색문제라고 볼 수 있겠음


import sys
input = sys.stdin.readline


def sol():
    n = int(input())

    cnt = 0
    while True:
        if n == 0:
            print(cnt)
            break
        if n >= 5 and (n % 5) % 3 == 0:
            cnt += 1
            n = n - 5
        elif n >= 3:
            cnt += 1
            n = n - 3
        else:
            print(-1)
            break


sol()

# 골드5-문자열-소수&팰린드롬

import sys
input = sys.stdin.readline


def sol():
    n = int(input())

    big_int = 2000000
    numbers = [0] * (big_int + 1)
    numbers[1] = 1
    m = int(big_int ** 0.5)

    # 에라토스테네스 체 활용 소수 찾기
    for i in range(2, m + 1):
        if numbers[i] == 0:
            for j in range(i+i, big_int + 1, i):
                numbers[j] = 1

                # 문자열로 변환 후 리버싱해서 일치하는지 판별
    for i in range(n, big_int+1):
        if numbers[i] == 0 and str(i) == str(i)[::-1]:
            print(i)
            break


sol()

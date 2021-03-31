# 박진호 구글링 풀이

import sys
input = sys.stdin.readline


def sol():
    t = int(input())

    for _ in range(t):
        n = int(input())
        target = []
        for _ in range(n):
            target.append(input().strip())
        target.sort()  # 문자열 리스트 정렬하면 길이 상관없이 사전순으로 정렬됨
        flag = False
        for i in range(n-1):
            tmp_len = len(target[i])

            # 사전순 정렬되었으므로 인접한 원소만 비교하면 됨 (현재 원소의 길이만큼)
            if target[i] == target[i+1][:tmp_len]:
                flag = True
        if flag:
            print("NO")
        else:
            print("YES")


sol()

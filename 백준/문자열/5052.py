# 골드5-문자열-전화번호목록
# 출제의도는 트라이 자료구조를 활용하라는 거 같은데 걍 안함
# 문자열 리스트 정렬하면 사전순 정렬되는 게 핵심
# 정렬되었으면 인접원소만 비교하면 된다..


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

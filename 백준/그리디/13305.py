# 실버4 - 주유소
# 그리디

# 완탐 TLE
# dp 문제를 쪼갤 수 없음
# 이분탐색 할만한데 헬퍼 함수 작성하기가 쉽지 않음
# -> 그리디다

# ****
# 나는 sort해서 풀었지만 굳이 그럴 필요 없이
# min value를 갱신해나가며 값을 더해주면 된다.
# 주의할 점은 첫번째 주유소는 무조건 기름 채워야함.


n = int(input())
load_len = list(map(int, input().split()))
gas_station = list(map(int, input().split()))
check = [0]*n

sorted_gas = [(so, i) for i, so in enumerate(gas_station[:n-1])]
sorted_gas.sort()

res = 0
for so, i in sorted_gas:
    tmp = 0
    for j in range(i, n-1):
        if check[j] == 1:
            break
        check[j] = 1
        tmp += load_len[j]
    res += tmp * so

print(res)

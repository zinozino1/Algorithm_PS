# 1. defaultdict이용하기

# 기존에는 디폴트값이 없을 경우 오류가 발생하여 dict 생성해서
# 초기값으로 [] 넣어주고 그다음에 append했었는데
# defaultdict는 넣어줄 필요가 없다

from collections import defaultdict

dic = defaultdict(list)


# 2. 문자열 개별 정렬
a = ["cde", "cfc", "abc"]
print(sorted(a, key=lambda x: (x[0], x[-1])))
# => ["abc", "cfc", "cde"]


# 3.  knapsack 문제 종류
1. unbounded knapsack
-> 모든 종류의 물건이 무한대로 있을 때
-> 일차원 dp 정방향 순회로 해결 가능

2. bounded knapsack
-> 모든 종류의 물건의 수가 제한되어 있을 때
-> 모든 종류의 물건 수가 하나일 경우(-> 이차원 dp or 1차원 dp + 역순 순회로 해결 가능)

3. 0/1 knapsack
-> 모든 종류의 물건이 0개 or 1개 밖에 없을 때

4. fractional knapsack
-> 물건을 쪼개서 취할 수 있을 때
-> greedy + dp로 해결 가능

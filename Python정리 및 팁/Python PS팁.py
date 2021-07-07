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

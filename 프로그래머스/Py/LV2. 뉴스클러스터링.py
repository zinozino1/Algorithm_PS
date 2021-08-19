# 문자열 문제 상당히 고전함..
# 우선 쓸데없는 변수들이 너무 많다 반복문 안에서 처리할 수 있는데도 불구하고


def solution(str1, str2):
    s1, s2 = str1.lower(), str2.lower()
    res1, res2 = [], []
    tmp1, tmp2 = '', ''
    cnt1, cnt2 = 0, 0

    for i in range(len(s1)):
        if s1[i].isalpha():
            tmp1 += s1[i]
            cnt1 += 1
            if cnt1 == 2:
                res1.append(tmp1)
                tmp1 = s1[i]
                cnt1 = 1
        else:
            cnt1 = 0
            tmp1 = ''
    for i in range(len(s2)):
        if s2[i].isalpha():
            tmp2 += s2[i]
            cnt2 += 1
            if cnt2 == 2:
                res2.append(tmp2)
                tmp2 = s2[i]
                cnt2 = 1
        else:
            cnt2 = 0
            tmp2 = ''

    if len(set(res1) | set(res2)) == 0:
        return 65536

    # 합집합과 교집합 구하기 -> set으로 하면 중복되는 문자들이 날라가는 문제가 있음 -> 딕셔너리로 해결
    else:
        dic1, dic2 = {}, {}
        for r in res1:
            dic1[r] = dic1.get(r, 0)+1
        for r in res2:
            dic2[r] = dic2.get(r, 0)+1
        kyo = 0
        for d in dic1.keys():
            if dic2.get(d):
                kyo += min(dic1[d], dic2.get(d))
        return int(65536 * kyo/(len(res1)+len(res2)-kyo))


# 고수 풀이 중 일부
str1 = "asdfasdf asdfasfd fd"
str2 = " ddsa fdsadf "


list_str1 = []
list_str2 = []

# zip함수를 이용하면 pair로 출력 가능, str1[1:] -> 주의
for s1, slice_s1 in zip(str1, str1[1:]):
    print(s1, slice_s1)
    join_str = "".join([s1, slice_s1])  # join의 인자는 리스트가 와야함
    if join_str.isalpha():
        list_str1.append(join_str.lower())

for s2, slice_s2 in zip(str2, str2[1:]):  # str2 문자만 2글자씩 뽑기
    join_str = "".join([s2, slice_s2])
    if join_str.isalpha():
        list_str2.append(join_str.lower())

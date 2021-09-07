# 문자열 + set

from collections import Counter


def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    str1_set = []
    str2_set = []
    for i in range(len(str1)-1):
        if not str1[i].isalpha() or not str1[i+1].isalpha():
            continue
        str1_set.append(str1[i:i+2])

    for i in range(len(str2)-1):
        if not str2[i].isalpha() or not str2[i+1].isalpha():
            continue
        str2_set.append(str2[i:i+2])

    c1 = Counter(str1_set)
    c2 = Counter(str2_set)
    intersection = []
    union = []

    # 교집합
    for key in c1.keys():
        if key in c2:
            for i in range(min(c1[key], c2[key])):
                intersection.append(key)

    # 합집합
    for key in c1.keys():
        if key in c2:
            for i in range(max(c1[key], c2[key])):
                union.append(key)
            c1[key] = 0
            c2[key] = 0
    for key in c1.keys():
        if c1[key] != 0:
            for i in range(c1[key]):
                union.append(key)
    for key in c2.keys():
        if c2[key] != 0:
            for i in range(c2[key]):
                union.append(key)

    if len(intersection) == 0 and len(union) == 0:
        return 65536
    elif len(intersection) == 0 and len(union) != 0:
        return 0
    else:
        return int((len(intersection) / len(union)) * 65536)

# 개선된 풀이


def solution2(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    str1_set = []
    str2_set = []
    for i in range(len(str1)-1):
        if not str1[i].isalpha() or not str1[i+1].isalpha():
            continue
        str1_set.append(str1[i:i+2])

    for i in range(len(str2)-1):
        if not str2[i].isalpha() or not str2[i+1].isalpha():
            continue
        str2_set.append(str2[i:i+2])

    intersection = set(str1_set) & set(str2_set)
    union = set(str1_set) | set(str2_set)

    inter_sum = sum([min(str1_set.count(inter), str2_set.count(inter))
                     for inter in intersection])
    union_sum = sum([max(str1_set.count(u), str2_set.count(u)) for u in union])

    if union_sum == 0:
        return 65536
    return int(inter_sum / union_sum * 65536)

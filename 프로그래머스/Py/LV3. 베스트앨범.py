# 해시 문제
# 중간에 인덱스 실수해서 뻘짓함
# 딕셔너리에 배열 넣으려면 먼저 빈배열 전처리 해줘야함

def solution(genres, plays):

    pre_dict, score_dict = {}, {}
    for g in genres:
        score_dict[g] = []
    for g, p in zip(genres, plays):
        pre_dict[g] = pre_dict.get(g, 0)+p
    for i, v in enumerate(plays):
        score_dict[genres[i]].append((v, i))
    for s in score_dict.keys():
        score_dict[s] = sorted(
            score_dict[s], key=lambda x: (x[0], -x[1]), reverse=True)
    tmp = []
    for k, v in pre_dict.items():
        tmp.append((k, v))

    tmp.sort(key=lambda x: (x[1]), reverse=True)
    res = []

    for t in tmp:
        if len(score_dict[t[0]]) >= 2:
            res.append(score_dict[t[0]][0][1])
            res.append(score_dict[t[0]][1][1])
        else:
            res.append(score_dict[t[0]][0][1])

    return res

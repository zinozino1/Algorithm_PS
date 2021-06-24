# 무난한 문자열 + 해시 문제

def solution(n, words):
    res = []
    word_dic = {}
    user_cnt = [0] * n
    curr_people_num = 0
    for i in range(len(words)):
        if word_dic.get(words[i]) == 1 or i != 0 and words[i][0] != words[i-1][len(words[i-1])-1]:
            res.append(curr_people_num)
            res.append(user_cnt[curr_people_num])
            break
        else:
            word_dic[words[i]] = 1
        user_cnt[curr_people_num] += 1
        curr_people_num = (curr_people_num + 1) % n
    if not res:
        return [0, 0]
    else:
        return list(map(lambda x: x+1, res))

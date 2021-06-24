# 정확성은 통과했으나 효율성 실패
# 다시 도전해볼것

def delete_and(arr):
    res = []
    for i in range(len(arr)):
        tmp = []
        for j in range(len(arr[i])):
            if arr[i][j] != "and":
                tmp.append(arr[i][j])
        res.append(tmp)
    return res


def parse_string(arr):
    parsed_arr = []
    for i in range(len(arr)):
        parsed_arr.append(arr[i].split())
    return parsed_arr


def solution(info, query):
    parsed_info, parsed_query = parse_string(
        info), delete_and(parse_string(query))
    res = []
    for i in range(len(parsed_query)):
        outer_cnt = 0
        for j in range(len(parsed_info)):
            inner_cnt = 0
            for k in range(len(parsed_info[j])):
                if parsed_query[i][k] == "-":
                    inner_cnt += 1
                elif k == 4 and int(parsed_info[j][k]) >= int(parsed_query[i][k]):
                    inner_cnt += 1
                elif parsed_query[i][k] == parsed_info[j][k]:
                    inner_cnt += 1
            if inner_cnt > 4:
                outer_cnt += 1

        res.append(outer_cnt)

    return res

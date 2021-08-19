# 해시 + dfs
def solution(orders, course):

    menu_dic = {}

    def dfs(L, s, res):
        if L == k:
            tmp = "".join(sorted(res))
            menu_dic[tmp] = menu_dic.get(tmp, 0)+1
            return
        else:
            for i in range(s, len(o)):
                dfs(L+1, i+1, res+o[i])

    for o in orders:
        for k in range(2, len(o)+1):  # 재귀 트리 depth 제한 loop
            dfs(0, 0, '')

    res = []
    for c in course:
        max_value = -1e9
        for m in menu_dic.keys():
            if len(m) == c and menu_dic[m] > max_value:
                max_value = menu_dic[m]

        for m in menu_dic.keys():
            if len(m) == c and menu_dic[m] == max_value and max_value != 1:
                res.append(m)

    return sorted(res)

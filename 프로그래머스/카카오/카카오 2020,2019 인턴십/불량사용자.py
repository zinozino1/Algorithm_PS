import itertools as it


def solution(user_id, banned_id):
    s = set()
    cnt = 0
    for tmp in it.permutations(user_id, len(banned_id)):
        visited = [0]*len(banned_id)
        for i in range(len(tmp)):
            flag = True
            for j in range(len(banned_id)):
                if visited[j] == 1:
                    continue
                if len(tmp[i]) == len(banned_id[j]):
                    for k in range(len(tmp[i])):
                        if banned_id[j][k] != "*" and tmp[i][k] != banned_id[j][k]:
                            flag = False
                            break
                else:
                    continue
                if flag and visited[j] == 0:
                    visited[j] = 1
                    break

        if all(v == 1 for v in visited):
            curr = list(tmp)
            curr.sort()
            s.add(''.join(curr))
            cnt += 1

    return len(s)


def solution2(user_id, banned_id):

    ans = set()

    for tmp in it.permutations(user_id, len(banned_id)):

        banned = []
        check = [0]*len(banned_id)
        for ban in banned_id:

            outer_flag = False
            for i, t in enumerate(tmp):
                if len(t) != len(ban):
                    continue  # 길이 다를 경우
                if check[i] == 1:
                    continue  # 이미 체크 했다면
                for j in range(len(t)):
                    if ban[j] != t[j]:
                        if ban[j] == "*":
                            pass
                        else:
                            break
                else:
                    check[i] = 1
                    banned.append(t)
                    break

        if len(banned) == len(banned_id):
            ans.add(tuple(sorted(banned)))

    return len(ans)

import itertools as it


def solution(relation):
    zip_relation = []
    for r in zip(*relation):
        zip_relation.append(r)

    candidate_key = set()

    for i in range(1, len(zip_relation)+1):
        for keys in it.combinations(range(len(zip_relation)), i):
            duplicate = set()
            for j in range(len(zip_relation[0])):
                curr = []
                for k in keys:
                    curr.append(zip_relation[k][j])
                duplicate.add(tuple(curr))

            if len(duplicate) == len(zip_relation[0]):
                if len(keys) == 1:
                    candidate_key.add(keys)
                else:
                    for can in candidate_key:
                        cnt = 0
                        for k in can:
                            if k in keys:
                                cnt += 1
                        if cnt == len(can):
                            break
                    else:
                        candidate_key.add(keys)

    return len(candidate_key)

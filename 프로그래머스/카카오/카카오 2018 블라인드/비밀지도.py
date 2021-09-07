def solution(n, arr1, arr2):
    tmp_arr1 = []
    tmp_arr2 = []

    for a in arr1:
        tmp_arr1.append(str(bin(a)[2:]) if len(
            str(bin(a)[2:])) == n else "0"*(n-len(str(bin(a)[2:])))+str(bin(a)[2:]))
    for a in arr2:
        tmp_arr2.append(str(bin(a)[2:]) if len(
            str(bin(a)[2:])) == n else "0"*(n-len(str(bin(a)[2:])))+str(bin(a)[2:]))

    res = []
    for i in range(n):
        tmp = ''
        for j in range(n):
            if tmp_arr1[i][j] == "0" and tmp_arr2[i][j] == "0":
                tmp += ' '
            else:
                tmp += "#"
        res.append(tmp)

    return res

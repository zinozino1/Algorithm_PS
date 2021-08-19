def solution(n, arr1, arr2):

    def to_bin(arr):
        res = []
        for i in range(n):
            if len(str(bin(arr[i]))[2:]) < n:
                res.append(
                    "0"*(n-len(str(bin(arr[i]))[2:])) + str(bin(arr[i]))[2:])
            else:
                res.append(str(bin(arr[i]))[2:])
        return res

    def to_sharp(arr):
        res = []
        for a in arr:
            tmp = ''
            for c in a:
                if c == "0":
                    tmp += "@"
                else:
                    tmp += "#"
            res.append(tmp)
        return res
    res1, res2 = to_sharp(to_bin(arr1)), to_sharp(to_bin(arr2))

    final = []
    for i in range(n):
        tmp = ''
        for j in range(n):
            if res1[i][j] == "#" or res2[i][j] == "#":
                tmp += "#"
            else:
                tmp += " "
        final.append(tmp)

    return final

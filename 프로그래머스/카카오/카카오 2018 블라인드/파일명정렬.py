# 문자열 + 정렬

# split, replace에 횟수 적용가능..

def solution(files):
    tmp = []
    for idx, file in enumerate(files):
        head, number, tail = '', '', ''

        tmp_number = ''
        alpha_cnt = 0
        for i, f in enumerate(file):
            if f.isdigit() and alpha_cnt == 1:
                tmp_number += f
            elif not f.isdigit() and alpha_cnt == 0:
                alpha_cnt += 1
            elif not f.isdigit() and file[i-1].isdigit():
                alpha_cnt += 1

        head = file.split(tmp_number, 1)[0]
        number = tmp_number
        tail = file.split(tmp_number, 1)[1]

        tmp.append([head, number, tail, idx])

    tmp.sort(key=lambda x: (x[0].upper(), int(x[1]), x[3]))

    res = []
    for i in range(len(tmp)):
        curr = ""
        for j in range(len(tmp[i])-1):
            curr += str(tmp[i][j])
        res.append(curr)

    return res

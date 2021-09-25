def solution(enter, leave):

    in_ptr = 0
    out_ptr = 0
    room = []
    res = [0] * (len(enter)+1)
    while True:
        if in_ptr > len(enter)-1 and out_ptr > len(enter)-1:
            break
        if leave[out_ptr] in room:
            for r in room:
                if r != leave[out_ptr]:
                    res[r] += 1
                    res[leave[out_ptr]] += 1
            room.remove(leave[out_ptr])
            out_ptr += 1
        else:
            room.append(enter[in_ptr])
            in_ptr += 1

    return res[1:]

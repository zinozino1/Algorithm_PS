# 해쉬+문자열

def solution(record):

    user = {}
    messages = []
    res = []

    for r in record:
        tmp = r.split()
        if tmp[0] == "Enter":
            user[tmp[1]] = tmp[2]
            messages.append([tmp[1], "Enter"])
        elif tmp[0] == "Leave":
            messages.append([tmp[1], "Leave"])
        elif tmp[0] == "Change":
            user[tmp[1]] = tmp[2]

    for m in messages:
        id, oper = m[0], m[1]
        if oper == "Enter":
            res.append(user[id]+"님이 들어왔습니다.")
        elif oper == "Leave":
            res.append(user[id]+"님이 나갔습니다.")

    return res

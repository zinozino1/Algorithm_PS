def solution(new_id):
    # 1단계
    new_id = new_id.lower()

    # 2단계
    tmp = ''
    for n in new_id:
        if n.isalpha() or n.isdigit() or n == "-" or n == "_" or n == ".":
            tmp += n
    tmp = list(tmp)

    # 3단계

    # 3-1 stack 두번째 버전 -> 빈스택으로 시작

    stack2 = []
    for i in range(len(tmp)):
        stack2.append(tmp[i])
        if stack2 and len(stack2) >= 2:
            ss = stack2[len(stack2)-2:len(stack2)]
            if ''.join(ss) == "..":
                cnt = 0
                while stack2:
                    if cnt == 2:
                        break
                    stack2.pop()
                    cnt += 1
                stack2.append('.')
    tmp = stack2

    # 3-2 stack 첫번째 버전 -> 넣어서 시작 : 이게 더 효율적인듯

    # stack = list(tmp)[::-1]
    # tmp = []
    # while stack:
    #     curr = stack.pop()
    #     if curr == ".":
    #         if stack and stack[-1] == ".":
    #             stack.pop()
    #             stack.append(curr)
    #         else:
    #             tmp.append(curr)
    #     else:
    #         tmp.append(curr)

    # 4단계
    if tmp[0] == "." and tmp[-1] != ".":
        tmp = tmp[1:len(tmp)]
    elif tmp[-1] == "." and tmp[0] != ".":
        tmp = tmp[:len(tmp)-1]
    elif tmp[0] == "." and tmp[-1] == ".":
        tmp = tmp[1:len(tmp)-1]

    # 5단계
    if not tmp:
        tmp = ["a"]

    # 6단계
    if len(tmp) > 15:
        tmp = tmp[:15]
        if tmp[-1] == ".":
            tmp = tmp[:len(tmp)-1]

    # 7단계
    res = tmp[:]
    if len(tmp) < 3:
        while True:
            if len(res) == 3:
                break
            res.append(tmp[-1])
    res = "".join(res)
    return res

# 고수 풀이


def solution2(new_id):
    # 1단계
    new_id = new_id.lower()
    # 2단계
    answer = ''
    for word in new_id:
        if word.isalnum() or word in '-_.':
            answer += word
    # 3단계
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4단계
    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer
    # 5단계
    answer = 'a' if answer == '' else answer
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7단계
    if len(answer) <= 3:
        answer = answer + answer[-1] * (3-len(answer))
    return answer

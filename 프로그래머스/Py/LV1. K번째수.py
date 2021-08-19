# 정렬
# 매우 간단하나 인덱스 실수 조심할 것

def solution(array, commands):
    answer = []

    for i in range(len(commands)):
        tmp = array[commands[i][0]-1:commands[i][1]]
        tmp.sort()
        answer.append(tmp[commands[i][2]-1])
    print(answer)

    return answer

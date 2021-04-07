# 해시, 정렬
# 문자열 리스트 정렬하면 무조건 prefix끼리 뭉쳐있게 되어있다.
# 따라서 정렬한 후 인접한 것들만 비교하면 접두어 검사 완료

def solution(phone_book):

    phone_book.sort()
    answer = True
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
            break

    return answer

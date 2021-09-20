# 문자열
# 풀이시간 : 약 30분

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        res = []
        tmp_letters, tmp_digit = [], []
        for log in logs:
            tmp = (log.split(" ")[0], " ".join(
                log.split(" ")[1:len(log.split(" "))]))
            if tmp[1][0].isalpha():
                tmp_letters.append(tmp)
            else:
                tmp_digit.append(tmp)

        tmp_letters.sort(key=lambda x: (x[1], x[0]))

        for tl in tmp_letters:
            res.append(" ".join(list(tl)))
        res += [" ".join(td) for td in tmp_digit]
        return res

# 조금 더 간결한 풀이


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        tmp_letters, tmp_digit = [], []
        for log in logs:
            if log.split()[1].isalpha():
                tmp_letters.append(log)
            else:
                tmp_digit.append(log)
        tmp_letters.sort(key=lambda x: (x.split()[1:], x.split()[0])) -> 배열 정렬도 가능하구나..
        return tmp_letters + tmp_digit

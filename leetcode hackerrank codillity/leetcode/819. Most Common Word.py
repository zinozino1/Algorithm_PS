# 문자열
# 풀이시간 : 14분

from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.replace("!", " ").replace("?", " ").replace(
            "'", " ").replace(",", " ").replace(";", " ").replace(".", " ")
        paragraph = list(paragraph.lower().split())
        return sorted([item for item in Counter(paragraph).items() if item[0] not in banned], reverse=True, key=lambda x: (x[1]))[0][0]

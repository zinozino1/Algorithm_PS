# 정렬 -> 못품
# 모든 수에 어떤 적절한 변형을 줘야 풀 수 있음 => 테크닉 외워두자


# 풀이 1
# 모든 숫자를 같은 자리 (4자리)로 맞춰줌
def solution(numbers):
    l = []

    for number in numbers:
        original = str(number)
        number = list(str(number))
        i = 0
        while len(number) <= 4:
            number.append(original[i])
            i = (i + 1) % len(original)
        number = int("".join(number))
        l.append([number, original])

    l = sorted(l, reverse=True)
    # join은 이렇게 쓰는 것
    return str(int("".join([item[1] for item in l])))


# 풀이 2
# 모든 숫자를 그냥 *3함 => 파이썬 문자열 비교는 숫자형과 달리 첫글자가 큰 순서대로, 문자열의 길이가 긴 순서대로 정렬되기 때문
def solution2(numbers):
    numbers = list(map(str, numbers))
    # 문자열 정렬.
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

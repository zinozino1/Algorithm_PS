# - 2. 카카오 스포츠 경기
# - 라이언 왕국와 어피치 왕국은 스포츠 경기 대결을 하고 싶어함
# - 어피치 왕국은 경기를 이기기 위해 팀의 전력을 최대로 만들고 싶어함
# - 각 선수는 1, 2, 3…으로 증가하는 고유한 공격력이 부여되어있습니다.
# - 팀의 출전 명단은 한 명의 선수에서부터 시작하여 다음과 같은 방법으로 출전하는 선수의 수가 증가함

# - 처음 팀에 x 공격력을 가진 선수 한명이 있음
# - x의 각 자릿수의 계승 합이 y가 됨. 그러면 y 공격력을 가진 선수를 출전 명단에 추가함
# - 마찬가지로 y의 각 자리수의 계승 합인 z 공격력을 가진 선수를 출전 명단에 추가함
# - 하지만, 이미 동일한 공격력을 가진 선수는 다시 추가할 수 없음

# - 최대 공격력을 가진 선수가 팀 리더가 되며, 팀 리더의 공격력과 팀 선수들의 수를 곱한 값이 팀의 전력이 됨
# - 첫 선수의 공격력 x가 주어졌을 때, 팀의 전력을 구한 후 그 값을 반환

#- 예제
# - 예를 들어, 한 선수의 공격력이 24이면 다음 출전 선수의 공격력은 26이 됨
# (두 번째 자리수) 2의 계승 + (첫 번째 자리수) 4의 계승 = 2! + 4! = 2 * 1 + 4 * 3 * 2 * 1 = 26

# - 출전 선수들의 공격력이 {4, 24, 26, 722, 5044, 169, 363601 ,1454} 라면
# - 이 팀의 전력은 2908808이 됨
# 363601 * 8 = 2908808

arr1 = [4, 24, 26, 722, 5044, 169, 363601, 1454]
p1 = arr1[0]


def get_factorial(num):
    if num == 1:
        return 1
    return num * get_factorial(num-1)


def sol(p, arr):

    check = set()  # 출전 선수 명단
    check.add(p)

    target = str(p)

    while True:
        target_num = 0
        for i in range(len(target)):
            if int(target[i]) == 0:
                target_num += 1
            else:
                target_num += get_factorial(int(target[i]))

        if target_num not in check and target_num in arr:
            check.add(target_num)
            target = str(target_num)

        else:
            break

    return max(check)*len(check)


print(sol(p1, arr1))

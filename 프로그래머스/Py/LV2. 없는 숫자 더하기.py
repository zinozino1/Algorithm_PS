def solution(numbers):
    res = 0
    numbers.sort()
    if len(numbers) == 1:
        return 45-numbers[0]

    for i, n in enumerate(numbers):
        diff = 0
        if i == 0:
            if n != 0:
                diff = n
                for j in range(diff):
                    res += j

        else:
            if i == len(numbers) - 1:
                if n != 9:
                    diff = 9-n
                    prev = n+1
                    for j in range(diff):
                        res += prev
                        prev += 1

            if numbers[i-1] + 1 != n:
                diff = n - numbers[i-1]
                prev = numbers[i-1] + 1
                for j in range(diff-1):
                    res += prev
                    prev += 1

    return res

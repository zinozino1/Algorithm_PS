# 구현 + 큐


from collections import deque


def solution(cacheSize, cities):

    cache = deque()
    ans = 0
    for city in cities:

        if city.upper() in cache:
            cache.remove(city.upper())
            cache.append(city.upper())
            ans += 1
        else:
            if len(cache) < cacheSize:
                cache.append(city.upper())
            else:
                if cache:
                    cache.popleft()
                    cache.append(city.upper())
            ans += 5

    return ans

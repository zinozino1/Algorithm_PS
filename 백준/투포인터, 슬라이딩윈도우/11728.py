# 실버5 - 두 배열 합치기
# 투포인터


n, m = map(int, input().split())
arr1 = sorted(list(map(int, input().split())))
arr2 = sorted(list(map(int, input().split())))

lt = 0
rt = 0
res = []
while lt <= len(arr1)-1 and rt <= len(arr2)-1:
    if arr1[lt] > arr2[rt]:
        res.append(arr2[rt])
        rt += 1
    elif arr1[lt] < arr2[rt]:
        res.append(arr1[lt])
        lt += 1
    else:
        res.append(arr1[lt])
        res.append(arr2[rt])
        lt += 1
        rt += 1

if lt <= len(arr1):
    for i in range(lt, len(arr1)):
        res.append(arr1[i])
if rt <= len(arr2):
    for i in range(rt, len(arr2)):
        res.append(arr2[i])

print(*res)

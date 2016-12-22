def counting_sort(arr: list, k: int) -> list:
    pos = [0 for i in range(k)]
    for i in range(len(arr)):
        pos[arr[i]] += 1
    # pos contains count of each key
    index = len(arr)
    for i in reversed(range(len(pos))):
        pos[i] = index - pos[i]
        index = pos[i]
    print(pos)
    out = arr[:]
    for elem in arr:
        out[pos[elem]] = elem
        pos[elem] += 1
    return out


print(counting_sort([5,1,2,3,5,4,0,1,5,4,6,2,3], 7))
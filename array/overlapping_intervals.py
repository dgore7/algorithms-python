def merge_intervals(intervals):
    intervals = sorted(intervals, key=lambda interval: interval[0], reverse=True)
    n = len(intervals)
    i = 0
    current = 1
    print(intervals)
    while current < n:
        if intervals[i][0] <= intervals[current][1]:
            intervals[i][0] = intervals[current][0]
            intervals[i][1] = max(intervals[i][1], intervals[current][1])
            current += 1
        else:
            i += 1
            current += 1
    return intervals[:i + 1]


print(merge_intervals([[1, 2], [3, 4], [5, 6], [7, 8]]))

def sum_of_intervals(intervals: list) -> int:
    intervals.sort()
    result = 0

    a, b = intervals[0][0], intervals[0][0]
    for interval in intervals:
        a, b = max(interval[0], b), max(interval[1], b)
        result += b - a

    return result


def sum_of_intervals2(intervals):
    res, top = 0, float("-inf")

    for a, b in sorted(intervals):
        if top < b:
            res, top = res + b - max(top, a), b

    return res


intervals = [
    [1, 5],
    [10, 20],
    [1, 6],
    [16, 19],
    [5, 11]
]
print(sum_of_intervals(intervals))
print(sum_of_intervals2(intervals))

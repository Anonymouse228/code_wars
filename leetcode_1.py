def merge(nums_1: list[int], m: int, nums_2: list[int], n: int) -> None:
    i, j, k = m - 1, n - 1, m + n - 1
    while j != -1:
        if i == -1 or nums_1[i] <= nums_2[j]:
            nums_1[k] = nums_2[j]
            j -= 1
        else:
            nums_1[k] = nums_1[i]
            i -= 1
        k -= 1


nums_1 = [1, 2, 3, 0, 0, 0]
merge(nums_1, 3, [2, 5, 6], 3)
print(nums_1)

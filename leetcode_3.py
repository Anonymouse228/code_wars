def remove_duplicates(nums):
    nums[:] = list(set(nums))
    nums.sort()
    return len(nums)


arr = [-1, 0, 0, 0, 0, 3, 3]
print(remove_duplicates(arr))
print(arr)

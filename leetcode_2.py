class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i, q = 0, 0
        while i < len(nums):
            if nums[i] == val:
                q += 1
                nums.pop(i)
            else:
                i += 1
        return q


solution = Solution()
arr = [0, 1, 2, 2, 3, 0, 4, 2]
print(solution.removeElement(arr, 2))
print(arr)

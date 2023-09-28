class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for count, i in enumerate(nums):
            if i == target:
                return count
            elif i > target:
                return count
            elif count >= len(nums) - 1:
                return count + 1

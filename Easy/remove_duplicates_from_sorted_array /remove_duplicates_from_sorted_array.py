class Solution:
    def removeDuplicates(self, nums) -> int:
        res = []
        for count, i in enumerate(nums):
            if count >= 0 and len(res) == 0:
                res.append(i)
            elif len(res) > 0 and i not in res:
                res.append(i)
        count = len(nums) - len(res)
        # for i in range(count):
        #     res.append('_')
        return count



nums = [1, 1, 2]
test = Solution()
print(test.removeDuplicates(nums))

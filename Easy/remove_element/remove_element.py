class Solution:
    def removeElement(self, nums, val) -> int:
        res = []
        for i in nums:
            if i != val:
                res.append(i)
                # count += 1
        return len(res)





nums = [3, 2, 2, 3]
val = 3
test = Solution()
print(test.removeElement(nums, val))

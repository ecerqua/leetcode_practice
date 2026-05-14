class Solution:
    def getConcatenation(self, nums):
        n = len(nums)
        ans = [0] * (2 * n)

        for i in range(2 * n):
            x = i % n
            j = nums[x]
            ans[i] = j



solution = Solution()
solution.getConcatenation([1,2,3,4])

class Solution():
    def findMaxConsecutiveOnes(self, nums):
        maxcount = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
                if count > maxcount:
                    maxcount = count
            else:
                count = 0
        return maxcount
        


solution = Solution()
tests = [[1,1,0,1,1,1], [1,0,1,1,0,1]]
test_answers = [3, 2]

for t, a in zip(tests, test_answers):
    print(f"{solution.findMaxConsecutiveOnes(t)}\n{a}")
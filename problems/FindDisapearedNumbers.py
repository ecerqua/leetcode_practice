class Solution():
    def findDissapearedNumbers(self, nums):
        n = len(nums)
        counts = {}
        answer = []
        for i in range(1, n + 1):
            counts[i] = 0
        for x in nums:
            counts[x] += 1
        for i in range(1, n + 1):
            if counts[i] == 0:
                answer.append(i)
        return answer

# Test cases
nums = [
    [4,3,2,7,8,2,3,1],
    [1,1]
    ]

ans = [
    [5,6],
    [2]
    ]

solution = Solution()
for num, ans in zip(nums, ans):
    print(f"{solution.findDissapearedNumbers(num)} - {ans}")


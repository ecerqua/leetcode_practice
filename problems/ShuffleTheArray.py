class Solution:
    def shuffle(self, nums):
        n = int(len(nums) / 2)
        x = 0
        y = n
        ans = [0] * (n * 2)
        for i in range(len(nums)):
            if i % 2 == 0:
                ans[i] = nums[x]
                x += 1
            else:
                ans[i]= nums[y]
                y+= 1
        return ans
    

solution = Solution()
tests = [[2,5,1,3,4,7], [1,2,3,4,4,3,2,1], [1,1,2,2]]
test_answers = [[2,3,5,4,1,7], [1,4,2,3,3,2,4,1], [1,2,1,2]]

for t, a in zip(tests, test_answers):
    print(f"{solution.shuffle(t)}: {a}")
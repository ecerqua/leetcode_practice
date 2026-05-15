class Solution():
    def smallerNumbersThanCurrent(self, nums):
        ans = [0] * len(nums) # initialize an empty list to store counts for each index
        for i in range(len(nums)): # iterate over index positions
            for x in nums: # iterate over nums values
                if nums[i] > x: # check if current nums value is greater than current x value: increment by one
                    ans[i] += 1
        return ans


# Testing
nums1 = [8,1,2,2,3]
ans1 = [4,0,1,1,3]

nums2 = [6,5,4,8]
ans2 = [2,1,0,3]

nums3 = [7,7,7,7]
ans3 = [0,0,0,0]

solution = Solution()

print(f"{solution.smallerNumbersThanCurrent(nums1)}\n{ans1}")
print(f"{solution.smallerNumbersThanCurrent(nums2)}\n{ans2}")
print(f"{solution.smallerNumbersThanCurrent(nums3)}\n{ans3}")
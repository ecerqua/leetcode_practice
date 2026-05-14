class Solution():
    def findErrorNums(self, nums):
        n = len(nums) # n = the length of nums
        counts = {} # initialize empty dictionary to count unique numbers in nums
        ans = [0] * 2 # initialize empty list for to store the answer
        for i in range(n): # for i in length of nums
            i += 1 # i = 1 + 1: because integers in the list start at 1
            counts[i] = 0 # create key for each int. Value starts at zero
        for x in nums: # iterate over nums list
            counts[x] += 1 # increment count in the dictionary.
        for i in range(n): # iterate over the dictionary values
            if counts[i + 1] == 0: # identify the missing value
                ans[1] = i + 1
            elif counts[i +1] == 2: # identify the duplicate value
                ans[0] = i +1
        return ans # return the answer

test = Solution()
nums = [1,1]
print(test.findErrorNums(nums))

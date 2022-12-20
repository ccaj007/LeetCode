nums = [1,2,3,4]

class Solution:

    def runningSum(self, nums):
        new = []
        total  = 0
        for i in range(len(nums)):
            total += nums[i]
            new.append(total)

        return(new)

s = Solution()
print(s)

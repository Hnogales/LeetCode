'''
Given an array nums.
We define a running sum of an array as runningSum[i] = sum(nums[0] … nums[i]).
Return the running sum of nums.
'''

class Solution(object):
    def runningSum(self, nums):
        # Variable initialized to store accumulated sum
        count = 0

        # iterating through list updating count and current item
        for i in range(len(nums)):
            # updating count with current number
            count  += nums[i]
            # setting current index to accumulated value
            nums[i] = count 

        return nums


sol = Solution()

# Example usage:
nums1 = [1, 2, 3, 4]
nums2 = [1, 1, 1, 1, 1]
nums3 = [3, 1, 2, 10, 1]

print(sol.runningSum(nums1))  # Output: [1, 3, 6, 10]
print(sol.runningSum(nums2))  # Output: [1, 2, 3, 4, 5]
print(sol.runningSum(nums3))  # Output: [3, 4, 6, 16, 17]

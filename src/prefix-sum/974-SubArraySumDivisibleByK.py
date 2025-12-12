class Solution(object):
    def SubArray(self, nums, k):
        prefix_sum = Solution().GetPrefixSum(nums)
        
        hashmap= {0:1}
        counter = 0

        for num in prefix_sum:
            reminder = num % k

            if reminder in hashmap:
                counter += hashmap[reminder]
                hashmap[reminder] += 1
            else:
                hashmap[reminder] = 1
        
        return counter


    def GetPrefixSum(self, nums):
        prefix_sum = [nums[0]]
        for index in range (1, len(nums)):
            prefix_sum.append(prefix_sum[index - 1] + nums[index])
        return prefix_sum

result = Solution().SubArray([4,5,0,-2,-3,1], 5)
print(result)
result = Solution().SubArray([5], 9)
print(result)
result = Solution().SubArray([1, 2, 3], 3)
print(result)


'''

974. Subarray Sums Divisible by K
Medium

Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.

********************************************************************************************************************** 

Example 1:

Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

Example 2:

Input: nums = [5], k = 9
Output: 0
 
Constraints:

1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
2 <= k <= 104

**********************************************************************************************************************

Approach:

1. Create a array with prefix sums
2. For each item in prefix sum array, 
    - divide by k 
    - check whether the reminder is in hashmap
    - if yes increment the counter by hashmap value against the reminder
    - else add the reminder to hashmap
3. Final value of the counter is the result

'''


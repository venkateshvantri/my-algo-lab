class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        prefix_sums = {0: 1}
        total_count = 0
        aggr_sum = 0

        for num in nums:
            aggr_sum += num
            if aggr_sum - k in prefix_sums:
                total_count += prefix_sums[aggr_sum - k]
            if aggr_sum in prefix_sums:
                prefix_sums[aggr_sum] += 1
            else:
                prefix_sums[aggr_sum] = 1
        
        return total_count

result =Solution().subarraySum([1, 1, 1], 2)
print(result)
result =Solution().subarraySum([1, 2, 3], 3)
print(result)


'''

560. Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2

Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

- 1 <= nums.length <= 2 * 10 power 4
- 1000 <= nums[i] <= 1000
- 10 power 7 <= k <= 10 power 7

****************************************************************************************************************

Approach:
- Substract each element of prefix_sum array with K and check whether the result is there in the hashmap
- if exists, then increment count by 1
- else add current prefix_sum array element to hashmap

'''
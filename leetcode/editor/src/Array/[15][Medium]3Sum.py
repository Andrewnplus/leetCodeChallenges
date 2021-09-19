# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k
# ]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. 
# 
#  Notice that the solution set must not contain duplicate triplets. 
# 
#  
#  Example 1: 
#  Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
#  Example 2: 
#  Input: nums = []
# Output: []
#  Example 3: 
#  Input: nums = [0]
# Output: []
#  
#  
#  Constraints: 
# 
#  
#  0 <= nums.length <= 3000 
#  -105 <= nums[i] <= 105 
#  
#  Related Topics Array Two Pointers Sorting 
#  👍 13005 👎 1261


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[tuple[int, int, int]]:
        triplets = []
        nums.sort()
        for index in range(len(nums) - 2):
            # Edge Case
            if nums[index] > 0:
                break
            # Skip the duplicated one
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            secondIndex = index + 1
            thirdIndex = len(nums) - 1
            # Edge Case
            if nums[thirdIndex] < 0:
                break
            while secondIndex < thirdIndex:
                toBeZeroSum = nums[index] + nums[secondIndex] + nums[thirdIndex]
                if toBeZeroSum < 0:
                    secondIndex += 1
                elif toBeZeroSum > 0:
                    thirdIndex -= 1
                else:
                    triplets.append((nums[index], nums[secondIndex], nums[thirdIndex]))
                    # Skip the duplicated one
                    while secondIndex < thirdIndex and nums[secondIndex] == nums[secondIndex + 1]:
                        secondIndex += 1
                    # Skip the duplicated one
                    while secondIndex < thirdIndex and nums[thirdIndex] == nums[thirdIndex - 1]:
                        thirdIndex -= 1
                    secondIndex += 1
                    thirdIndex -= 1
        return triplets

# leetcode submit region end(Prohibit modification and deletion)

# Given an integer array nums sorted in non-decreasing order, return an array 
# of the squares of each number sorted in non-decreasing order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  nums is sorted in non-decreasing order. 
#  
# 
#  
# Follow up: Squaring each element and sorting the new array is very trivial, 
# could you find an O(n) solution using a different approach? Related Topics Array 
# Two Pointers Sorting 👍 3855 👎 130


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        leftPoint, rightPoint = 0, n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[leftPoint]) <= abs(nums[rightPoint]):
                largerOne = nums[rightPoint]
                rightPoint -= 1
            else:
                largerOne = nums[leftPoint]
                leftPoint += 1
            result[i] = largerOne ** 2
        return result

# leetcode submit region end(Prohibit modification and deletion)

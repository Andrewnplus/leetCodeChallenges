# Given an array of integers nums which is sorted in ascending order, and an 
# integer target, write a function to search target in nums. If target exists, then 
# return its index. Otherwise, return -1. 
# 
#  You must write an algorithm with O(log n) runtime complexity. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -10⁴ < nums[i], target < 10⁴ 
#  All the integers in nums are unique. 
#  nums is sorted in ascending order. 
#  
#  Related Topics Array Binary Search 👍 2624 👎 80


# leetcode submit region begin(Prohibit modification and deletion)
import unittest
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        leftPoint, rightPoint = 0, len(nums) - 1
        while leftPoint <= rightPoint:
            pivot = leftPoint + (rightPoint - leftPoint) // 2
            if target == nums[pivot]:
                return pivot
            elif target < nums[pivot]:
                rightPoint = pivot - 1
            else:
                leftPoint = pivot + 1
        return -1


# leetcode submit region end(Prohibit modification and deletion)


class TestCase(unittest.TestCase):
    def testSearch_case1(self):
        nums = [2, 3, 4]
        target = 2
        expectedResult = 0

        self.assertEqual(Solution().search(nums, target), expectedResult)

    def testSearch_case2(self):
        nums = [2, 7, 11, 15]
        target = 9
        expectedResult = -1

        self.assertEqual(Solution().search(nums, target), expectedResult)

    def testSearch_case3(self):
        nums = [0, 3, 4]
        target = 3
        expectedResult = 1

        self.assertEqual(Solution().search(nums, target), expectedResult)


if __name__ == "__main__":
    unittest.main()

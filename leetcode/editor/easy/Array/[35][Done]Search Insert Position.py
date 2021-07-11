# Given a sorted array of distinct integers and a target value, return the index
#  if the target is found. If not, return the index where it would be if it were i
# nserted in order. 
# 
#  
#  Example 1: 
#  Input: nums = [1,3,5,6], target = 5
# Output: 2
#  Example 2: 
#  Input: nums = [1,3,5,6], target = 2
# Output: 1
#  Example 3: 
#  Input: nums = [1,3,5,6], target = 7
# Output: 4
#  Example 4: 
#  Input: nums = [1,3,5,6], target = 0
# Output: 0
#  Example 5: 
#  Input: nums = [1], target = 0
# Output: 0
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 104 
#  -104 <= nums[i] <= 104 
#  nums contains distinct values sorted in ascending order. 
#  -104 <= target <= 104 
#  
#  Related Topics Array Binary Search 
#  👍 3377 👎 287


# leetcode submit region begin(Prohibit modification and deletion)
import unittest
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        tempValue = target
        if target in nums:
            return nums.index(target)
        else:
            while tempValue not in nums and nums[-1] > tempValue:
                tempValue += 1
            while tempValue not in nums and nums[-1] < tempValue:
                tempValue -= 1
            if tempValue > target:
                return nums.index(tempValue)
            else:
                return nums.index(tempValue) + 1


# leetcode submit region end(Prohibit modification and deletion)
class TestCase(unittest.TestCase):

    def testAddBinary_case1(self):
        nums = [1, 3, 5, 6]
        target = 7
        expectedResult = 4

        self.assertEqual(Solution().searchInsert(nums, target), expectedResult)

    def testAddBinary_case2(self):
        nums = [1, 3, 5, 6]
        target = 2
        expectedResult = 1

        self.assertEqual(Solution().searchInsert(nums, target), expectedResult)

    def testAddBinary_case3(self):
        nums = [1, 3, 5, 6]
        target = 5
        expectedResult = 2

        self.assertEqual(Solution().searchInsert(nums, target), expectedResult)

    def testAddBinary_case4(self):
        nums = [1, 3, 5, 6]
        target = 0
        expectedResult = 0

        self.assertEqual(Solution().searchInsert(nums, target), expectedResult)

    def testAddBinary_case5(self):
        nums = [1]
        target = 0
        expectedResult = 0

        self.assertEqual(Solution().searchInsert(nums, target), expectedResult)


if __name__ == "__main__":
    unittest.main()

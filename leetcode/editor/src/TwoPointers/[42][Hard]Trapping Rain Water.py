# Given n non-negative integers representing an elevation map where the width of
#  each bar is 1, compute how much water it can trap after raining. 
# 
#  
#  Example 1: 
# 
#  
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [
# 0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are
#  being trapped.
#  
# 
#  Example 2: 
# 
#  
# Input: height = [4,2,0,3,2,5]
# Output: 9
#  
# 
#  
#  Constraints: 
# 
#  
#  n == height.length 
#  0 <= n <= 3 * 104 
#  0 <= height[i] <= 105 
#  
#  Related Topics Array Two Pointers Dynamic Programming Stack Monotonic Stack 
#  👍 12885 👎 186


# leetcode submit region begin(Prohibit modification and deletion)
import unittest
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        leftPointer = 0
        rightPointer = len(height) - 1
        maxVolume = 0
        maxLeftSide = 0
        maxRightSide = 0
        while leftPointer <= rightPointer:
            maxLeftSide = max(maxLeftSide, height[leftPointer])
            maxRightSide = max(maxRightSide, height[rightPointer])
            if maxLeftSide < maxRightSide:
                maxVolume += maxLeftSide - height[leftPointer]
                leftPointer += 1
            else:
                maxVolume += maxRightSide - height[rightPointer]
                rightPointer -= 1

        return maxVolume


# leetcode submit region end(Prohibit modification and deletion)


class TestCase(unittest.TestCase):

    def testTrap_1(self):
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        expectedResult = 6

        self.assertEqual(expectedResult, Solution().trap(height))

    def testTrap_2(self):
        height = [4, 2, 0, 3, 2, 5]
        expectedResult = 9

        self.assertEqual(expectedResult, Solution().trap(height))


if __name__ == "__main__":
    unittest.main()

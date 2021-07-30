# Given an array nums with n objects colored red, white, or blue, sort them in-p
# lace so that objects of the same color are adjacent, with the colors in the orde
# r red, white, and blue. 
# 
#  We will use the integers 0, 1, and 2 to represent the color red, white, and b
# lue, respectively. 
# 
#  You must solve this problem without using the library's sort function. 
# 
#  
#  Example 1: 
#  Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
#  Example 2: 
#  Input: nums = [2,0,1]
# Output: [0,1,2]
#  Example 3: 
#  Input: nums = [0]
# Output: [0]
#  Example 4: 
#  Input: nums = [1]
# Output: [1]
#  
#  
#  Constraints: 
# 
#  
#  n == nums.length 
#  1 <= n <= 300 
#  nums[i] is 0, 1, or 2. 
#  
# 
#  
#  Follow up: Could you come up with a one-pass algorithm using only constant ex
# tra space? 
#  Related Topics Array Two Pointers Sorting 
#  👍 6155 👎 332


# leetcode submit region begin(Prohibit modification and deletion)
import unittest
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        redPointer = 0
        whitePointer = 0
        bluePointer = len(nums) - 1
        while whitePointer <= bluePointer:
            # that's the missing point I lacked (2021.07.30)
            if nums[whitePointer] == 1:
                whitePointer += 1
            elif nums[whitePointer] == 0:
                nums[whitePointer], nums[redPointer] = nums[redPointer], nums[whitePointer]
                whitePointer += 1
                redPointer += 1
            else:
                nums[whitePointer], nums[bluePointer] = nums[bluePointer], nums[whitePointer]
                bluePointer -= 1
            # leetcode submit region end(Prohibit modification and deletion)


class TestCase(unittest.TestCase):

    def testMaxArea_1(self):
        nums = [2, 0, 2, 1, 1, 0]

        expectedResult = [0, 0, 1, 1, 2, 2]

    def testMaxArea_2(self):
        nums = [2, 0, 1]

        expectedResult = [0, 1, 2]

        print(Solution().sortColors(nums))

    def testMaxArea_3(self):
        nums = [0]

        expectedResult = [0]

    def testMaxArea_4(self):
        nums = [1]

        expectedResult = [1]


if __name__ == "__main__":
    unittest.main()

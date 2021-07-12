# Given a non-empty array of integers nums, every element appears twice except f
# or one. Find that single one. 
# 
#  Follow up: Could you implement a solution with a linear runtime complexity an
# d without using extra memory? 
# 
#  
#  Example 1: 
#  Input: nums = [2,2,1]
# Output: 1
#  Example 2: 
#  Input: nums = [4,1,2,1,2]
# Output: 4
#  Example 3: 
#  Input: nums = [1]
# Output: 1
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 3 * 104 
#  -3 * 104 <= nums[i] <= 3 * 104 
#  Each element in the array appears twice except for one element which appears 
# only once. 
#  
#  Related Topics Hash Table Bit Manipulation 
#  👍 5981 👎 197


# leetcode submit region begin(Prohibit modification and deletion)
import unittest
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = {}
        for num in nums:
            if num in result:
                result[num] += 1
            else:
                result[num] = 1
        return min(result, key=result.get)


# leetcode submit region end(Prohibit modification and deletion)

class TestCase(unittest.TestCase):

    def testSingleNumber_1(self):
        inputNums = [2, 2, 1]

        expectedResult = 1

        self.assertEqual(Solution().singleNumber(inputNums), expectedResult)

    def testSingleNumber_2(self):
        inputNums = [4, 1, 2, 1, 2]

        expectedResult = 4

        self.assertEqual(Solution().singleNumber(inputNums), expectedResult)

    def testSingleNumber_3(self):
        inputNums = [1]

        expectedResult = 1

        self.assertEqual(Solution().singleNumber(inputNums), expectedResult)


if __name__ == "__main__":
    unittest.main()

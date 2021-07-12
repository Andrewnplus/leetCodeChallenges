# Given a signed 32-bit integer x, return x with its digits reversed. If reversi
# ng x causes the value to go outside the signed 32-bit integer range [-231, 231 -
#  1], then return 0. 
# 
#  Assume the environment does not allow you to store 64-bit integers (signed or
#  unsigned). 
# 
#  
#  Example 1: 
#  Input: x = 123
# Output: 321
#  Example 2: 
#  Input: x = -123
# Output: -321
#  Example 3: 
#  Input: x = 120
# Output: 21
#  Example 4: 
#  Input: x = 0
# Output: 0
#  
#  
#  Constraints: 
# 
#  
#  -231 <= x <= 231 - 1 
#  
#  Related Topics Math 
#  👍 4413 👎 6809

import unittest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reverse(self, inputNumber: int) -> int:
        sign = [1, -1][inputNumber < 0]
        output = sign * int(str(abs(inputNumber))[::-1])

        return output if -(2 ** 31) - 1 < output < 2 ** 31 else 0


# leetcode submit region end(Prohibit modification and deletion)

class TestCase(unittest.TestCase):

    def testReverse_positiveNumber(self):
        inputNumber = 1230
        expectedResult = 321
        self.assertEqual(Solution().reverse(inputNumber), expectedResult)

    def testReverse_negativeNumber(self):
        inputNumber = -1230
        expectedResult = -321
        self.assertEqual(Solution().reverse(inputNumber), expectedResult)


if __name__ == "__main__":
    unittest.main()

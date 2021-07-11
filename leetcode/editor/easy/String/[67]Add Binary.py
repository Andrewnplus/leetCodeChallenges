# Given two binary strings a and b, return their sum as a binary string.
#
#
#  Example 1:
#  Input: a = "11", b = "1"
# Output: "100"
#  Example 2:
#  Input: a = "1010", b = "1011"
# Output: "10101"
#
#
#  Constraints:
#
#
#  1 <= a.length, b.length <= 104
#  a and b consist only of '0' or '1' characters.
#  Each string does not contain leading zeros except for the zero itself.
#
#  Related Topics Math String
#  👍 2576 👎 334


# leetcode submit region begin(Prohibit modification and deletion)


import queue


# This situation is good to use recursive.
import unittest
import queue


class Solution(object):
    def addBinary(self, binaryStringA: str, binaryStringB: str) -> str:
        if len(binaryStringA) == 0:
            return binaryStringB
        if len(binaryStringB) == 0:
            return binaryStringA
        if binaryStringA[-1] == '1' and binaryStringB[-1] == '1':
            return self.addBinary(self.addBinary(binaryStringA[0:-1], binaryStringB[0:-1]), "1") + "0"
        if binaryStringA[-1] == '0' and binaryStringB[-1] == '0':
            return self.addBinary(binaryStringA[0:-1], binaryStringB[0:-1]) + "0"
        else:
            return self.addBinary(binaryStringA[0:-1], binaryStringB[0:-1]) + "1"





# leetcode submit region end(Prohibit modification and deletion)


class TestCase(unittest.TestCase):

    def testAddBinary_1digitAnd2digits(self):
        binaryStringA = "1"
        binaryStringB = "11"
        expectedResult = "100"

        self.assertEqual(Solution().addBinary(binaryStringA, binaryStringB), expectedResult)

    def testAddBinary_2digits(self):
        binaryStringA = "1010"
        binaryStringB = "1011"
        expectedResult = "10101"

        self.assertEqual(Solution().addBinary(binaryStringA, binaryStringB), expectedResult)

    def testAddBinary_4digitAnd5Digit(self):
        binaryStringA = "10101"
        binaryStringB = "1111"
        expectedResult = "100100"

        self.assertEqual(Solution().addBinary(binaryStringA, binaryStringB), expectedResult)


if __name__ == "__main__":
    unittest.main()

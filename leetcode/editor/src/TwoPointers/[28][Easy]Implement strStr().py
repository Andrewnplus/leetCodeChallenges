# Implement strStr().
#
#  Return the index of the first occurrence of needle in haystack, or -1 if need
# le is not part of haystack.
#
#  Clarification:
#
#  What should we return when needle is an empty string? This is a great questio
# n to ask during an interview.
#
#  For the purpose of this problem, we will return 0 when needle is an empty str
# ing. This is consistent to C's strstr() and Java's indexOf().
#
#
#  Example 1:
#  Input: haystack = "hello", needle = "ll"
# Output: 2
#  Example 2:
#  Input: haystack = "aaaaa", needle = "bba"
# Output: -1
#  Example 3:
#  Input: haystack = "", needle = ""
# Output: 0
#
#
#  Constraints:
#
#
#  0 <= haystack.length, needle.length <= 5 * 104
#  haystack and needle consist of only lower-case English characters.
#
#  Related Topics Two Pointers String String Matching
#  👍 2610 👎 2525


# leetcode submit region begin(Prohibit modification and deletion)
import unittest


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1

        for index, item in enumerate(haystack):
            needleLength = len(needle)
            if index + len(needle) > len(haystack):
                return -1
            if haystack[index: index + needleLength] == needle:
                return index
        return -1

        # leetcode submit region end(Prohibit modification and deletion)


class TestCase(unittest.TestCase):

    def testStrStr_1(self):
        haystack = "hello"
        needle = "ll"

        expectedResult = 2

        self.assertEqual(Solution().strStr(haystack, needle), expectedResult)

    def testSingleNumber_2(self):
        haystack = "aaaaa"
        needle = "bba"

        expectedResult = -1

        self.assertEqual(Solution().strStr(haystack, needle), expectedResult)

    def testSingleNumber_3(self):
        haystack = ""
        needle = ""

        expectedResult = 0

        self.assertEqual(Solution().strStr(haystack, needle), expectedResult)

    def testSingleNumber_4(self):
        haystack = "mississippi"
        needle = "issip"

        expectedResult = 4

        self.assertEqual(Solution().strStr(haystack, needle), expectedResult)


if __name__ == "__main__":
    unittest.main()

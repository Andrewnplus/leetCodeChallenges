# Write a function to find the longest common prefix string amongst an array of 
# strings. 
# 
#  If there is no common prefix, return an empty string "". 
# 
#  
#  Example 1: 
# 
#  
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#  
# 
#  Example 2: 
# 
#  
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= strs.length <= 200 
#  0 <= strs[i].length <= 200 
#  strs[i] consists of only lower-case English letters. 
#  
#  Related Topics String 
#  👍 3902 👎 2182


# leetcode submit region begin(Prohibit modification and deletion)
import unittest
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortestWord = min(strs, key=len)
        for index, char in enumerate(shortestWord):
            for other in strs:
                if other[index] != char:
                    return shortestWord[:index]
        return shortestWord


# leetcode submit region end(Prohibit modification and deletion)


class TestCase(unittest.TestCase):

    def testLongestCommonPrefix_normalCase1(self):
        inputStringList = ["flower", "flow", "flight"]

        expectedResult = "fl"

        self.assertEqual(Solution().longestCommonPrefix(inputStringList), expectedResult)

    def testLongestCommonPrefix_noCommonPrefix(self):
        inputStringList = ["dog", "racecar", "car"]

        expectedResult = ""

        self.assertEqual(Solution().longestCommonPrefix(inputStringList), expectedResult)

    def testLongestCommonPrefix_normalCase2(self):
        inputStringList = ["aaaaa", "aaab", "aac"]

        expectedResult = "aa"

        self.assertEqual(Solution().longestCommonPrefix(inputStringList), expectedResult)


if __name__ == "__main__":
    unittest.main()

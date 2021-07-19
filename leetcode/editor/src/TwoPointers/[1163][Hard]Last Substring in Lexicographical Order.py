# Given a string s, return the last substring of s in lexicographical order. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "abab"
# Output: "bab"
# Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. 
# The lexicographically maximum substring is "bab".
#  
# 
#  Example 2: 
# 
#  
# Input: s = "leetcode"
# Output: "tcode"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 4 * 105 
#  s contains only lowercase English letters. 
#  
#  Related Topics Two Pointers String 
#  👍 351 👎 379


# leetcode submit region begin(Prohibit modification and deletion)
import unittest


class Solution:
    def lastSubstring(self, inputString: str) -> str:
        # Comparing to the subString with the same startIndex, longer is more suitable
        startIndexOfResult, startIndexOfCandidate, offset = 0, 1, 0
        while startIndexOfResult + offset < len(inputString) and startIndexOfCandidate + offset < len(inputString):

            if inputString[startIndexOfResult + offset] == inputString[startIndexOfCandidate + offset]:
                offset += 1
            else:
                if inputString[startIndexOfResult + offset] < inputString[startIndexOfCandidate + offset]:
                    startIndexOfResult += offset + 1
                else:
                    startIndexOfCandidate += offset + 1
                if startIndexOfResult == startIndexOfCandidate:
                    startIndexOfCandidate += 1
                offset = 0
        return inputString[startIndexOfResult:]


# leetcode submit region end(Prohibit modification and deletion)

class TestCase(unittest.TestCase):

    def testLastSubstring_1(self):
        inputString = "abab"
        expectedResult = "bab"

        self.assertEqual(Solution().lastSubstring(inputString), expectedResult)

    def testLastSubstring_2(self):
        inputString = "leetcode"
        expectedResult = "tcode"

        self.assertEqual(Solution().lastSubstring(inputString), expectedResult)


if __name__ == "__main__":
    unittest.main()

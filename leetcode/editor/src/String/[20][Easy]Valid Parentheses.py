# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']
# ', determine if the input string is valid. 
# 
#  An input string is valid if: 
# 
#  
#  Open brackets must be closed by the same type of brackets. 
#  Open brackets must be closed in the correct order. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: s = "()"
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: s = "()[]{}"
# Output: true
#  
# 
#  Example 3: 
# 
#  
# Input: s = "(]"
# Output: false
#  
# 
#  Example 4: 
# 
#  
# Input: s = "([)]"
# Output: false
#  
# 
#  Example 5: 
# 
#  
# Input: s = "{[]}"
# Output: true
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 104 
#  s consists of parentheses only '()[]{}'. 
#  
#  Related Topics String Stack 
#  👍 7109 👎 294


# leetcode submit region begin(Prohibit modification and deletion)
import unittest


class Solution:
    def isValid(self, parentheses: str) -> bool:
        if len(parentheses) % 2 != 0:
            return False
        parenthesesQueue = []
        for sign in parentheses:
            if sign == ")":
                if len(parenthesesQueue) == 0 or parenthesesQueue[-1] != "(":
                    return False
                else:
                    parenthesesQueue.pop(-1)
            if sign == "}":
                if len(parenthesesQueue) == 0 or parenthesesQueue[-1] != "{":
                    return False
                else:
                    parenthesesQueue.pop(-1)
            if sign == "]":
                if len(parenthesesQueue) == 0 or parenthesesQueue[-1] != "[":
                    return False
                else:
                    parenthesesQueue.pop(-1)
            if sign in ["(", "{", "["]:
                parenthesesQueue.append(sign)
        if len(parenthesesQueue) == 0:
            return True
        else:
            return False


# leetcode submit region end(Prohibit modification and deletion)
class TestCase(unittest.TestCase):

    def testIsValid_1(self):
        inputString = "())"
        expectedResult = False

        self.assertEqual(Solution().isValid(inputString), expectedResult)

    def testIsValid_2(self):
        inputString = "()[]{}"
        expectedResult = True

        self.assertEqual(Solution().isValid(inputString), expectedResult)

    def testIsValid_3(self):
        inputString = "(]"
        expectedResult = False

        self.assertEqual(Solution().isValid(inputString), expectedResult)

    def testIsValid_4(self):
        inputString = "([)]"
        expectedResult = False

        self.assertEqual(Solution().isValid(inputString), expectedResult)

    def testIsValid_5(self):
        inputString = "{[]}"
        expectedResult = True

        self.assertEqual(Solution().isValid(inputString), expectedResult)


if __name__ == "__main__":
    unittest.main()

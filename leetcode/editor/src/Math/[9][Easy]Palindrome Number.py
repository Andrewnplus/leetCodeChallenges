# Given an integer x, return true if x is palindrome integer. 
# 
#  An integer is a palindrome when it reads the same backward as forward. For ex
# ample, 121 is palindrome while 123 is not. 
# 
#  
#  Example 1: 
# 
#  
# Input: x = 121
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes
#  121-. Therefore it is not a palindrome.
#  
# 
#  Example 3: 
# 
#  
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#  
# 
#  Example 4: 
# 
#  
# Input: x = -101
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  -231 <= x <= 231 - 1 
#  
# 
#  
# Follow up: Could you solve it without converting the integer to a string? Rela
# ted Topics Math 
#  👍 3098 👎 1710


# leetcode submit region begin(Prohibit modification and deletion)
import unittest


class Solution:
    def isPalindrome(self, inputValue: int) -> bool:
        if inputValue < 0:
            return False
        if str(inputValue) == str(inputValue)[::-1]:
            return True

        return False

# leetcode submit region end(Prohibit modification and deletion)

class TestCase(unittest.TestCase):

    def testIsPalindrome_positiveNumber_NotPalindrome(self):
        inputValue = 123123
        expectedResult = False

        self.assertEqual(Solution().isPalindrome(inputValue), expectedResult)

    def testIsPalindrome_negativeNumber_NotPalindrome(self):
        inputValue = -123321
        expectedResult = False

        self.assertEqual(Solution().isPalindrome(inputValue), expectedResult)

    def testIsPalindrome_positiveNumber_palindrome(self):
        inputValue = 123321
        expectedResult = True

        self.assertEqual(Solution().isPalindrome(inputValue), expectedResult)


if __name__ == "__main__":
    unittest.main()
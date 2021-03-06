# Given an array nums and a value val, remove all instances of that value in-pla
# ce and return the new length. 
# 
#  Do not allocate extra space for another array, you must do this by modifying 
# the input array in-place with O(1) extra memory. 
# 
#  The order of elements can be changed. It doesn't matter what you leave beyond
#  the new length. 
# 
#  Clarification: 
# 
#  Confused why the returned value is an integer but your answer is an array? 
# 
#  Note that the input array is passed in by reference, which means a modificati
# on to the input array will be known to the caller as well. 
# 
#  Internally you can think of this: 
# 
#  
# // nums is passed in by reference. (i.e., without making a copy)
# int len = removeElement(nums, val);
# 
# // any modification to nums in your function would be known by the caller.
# // using the length returned by your function, it prints the first len element
# s.
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# } 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2]
# Explanation: Your function should return length = 2, with the first two elemen
# ts of nums being 2.
# It doesn't matter what you leave beyond the returned length. For example if yo
# u return 2 with nums = [2,2,3,3] or nums = [2,2,0,0], your answer will be accept
# ed.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3]
# Explanation: Your function should return length = 5, with the first five eleme
# nts of nums containing 0, 1, 3, 0, and 4. Note that the order of those five elem
# ents can be arbitrary. It doesn't matter what values are set beyond the returned
#  length.
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= nums.length <= 100 
#  0 <= nums[i] <= 50 
#  0 <= val <= 100 
#  
#  Related Topics Array Two Pointers 
#  👍 2038 👎 3444


# leetcode submit region begin(Prohibit modification and deletion)
import unittest
from typing import List


class Solution:
    def removeElement(self, inputNums: List[int], val: int) -> int:
        leftPointer = 0
        rightPointer = len(inputNums) - 1
        while leftPointer <= rightPointer:
            if inputNums[leftPointer] == val:
                inputNums[leftPointer], inputNums[rightPointer] = inputNums[rightPointer], inputNums[leftPointer]
                rightPointer -= 1
            else:
                leftPointer += 1
        return leftPointer


# leetcode submit region end(Prohibit modification and deletion)


class TestCase(unittest.TestCase):

    def testSingleNumber_1(self):
        inputNums = [3, 2, 2, 3]
        val = 3

        expectedResult = 2

        self.assertEqual(Solution().removeElement(inputNums, val), expectedResult)

    def testSingleNumber_2(self):
        inputNums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2

        expectedResult = 5

        self.assertEqual(Solution().removeElement(inputNums, val), expectedResult)


if __name__ == "__main__":
    unittest.main()

# Given a sorted array nums, remove the duplicates in-place such that each eleme
# nt appears only once and returns the new length. 
# 
#  Do not allocate extra space for another array, you must do this by modifying 
# the input array in-place with O(1) extra memory. 
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
# int len = removeDuplicates(nums);
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
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2]
# Explanation: Your function should return length = 2, with the first two elemen
# ts of nums being 1 and 2 respectively. It doesn't matter what you leave beyond t
# he returned length.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4]
# Explanation: Your function should return length = 5, with the first five eleme
# nts of nums being modified to 0, 1, 2, 3, and 4 respectively. It doesn't matter 
# what values are set beyond the returned length.
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= nums.length <= 3 * 104 
#  -104 <= nums[i] <= 104 
#  nums is sorted in ascending order. 
#  
#  Related Topics Array Two Pointers 
#  👍 3685 👎 6710


# leetcode submit region begin(Prohibit modification and deletion)
import unittest
from typing import List


class Solution:
    # # It will violate the extra space forbidden
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     countedValue = -105
    #     # use nums[:] will create a new array with the same value
    #     for num in nums[:]:
    #         if num == countedValue:
    #             nums.remove(num)
    #         else:
    #             countedValue = num
    #     return len(nums)

    def removeDuplicates(self, nums: List[int]) -> int:
        leftPointer = 0
        rightPointer = 1
        while rightPointer < len(nums):
            if nums[leftPointer] != nums[rightPointer]:
                nums[leftPointer + 1] = nums[rightPointer]
                leftPointer += 1
            rightPointer += 1
        return leftPointer + 1


# leetcode submit region end(Prohibit modification and deletion)
class TestCase(unittest.TestCase):

    def testIsValid_1(self):
        inputNums = [1, 1, 2]
        expectedResult = 2

        self.assertEqual(expectedResult, Solution().removeDuplicates(inputNums))
        print(inputNums)

    def testIsValid_2(self):
        inputNums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        expectedResult = 5

        self.assertEqual(expectedResult, Solution().removeDuplicates(inputNums))
        print(inputNums)


if __name__ == "__main__":
    unittest.main()

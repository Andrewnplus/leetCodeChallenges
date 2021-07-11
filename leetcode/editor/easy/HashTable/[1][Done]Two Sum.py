# Given an array of integers nums and an integer target, return indices of the t
# wo numbers such that they add up to target. 
# 
#  You may assume that each input would have exactly one solution, and you may n
# ot use the same element twice. 
# 
#  You can return the answer in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [3,3], target = 6
# Output: [0,1]
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= nums.length <= 103 
#  -109 <= nums[i] <= 109 
#  -109 <= target <= 109 
#  Only one valid answer exists. 
#  
#  Related Topics Array Hash Table 
#  👍 19685 👎 692


# leetcode submit region begin(Prohibit modification and deletion)
import unittest
from typing import List


# Key: there's definitely a solution with a pair, so save it as it's pair value by a map
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # the dictionary's key is the list's value and value is the list's key
        matchedDictionary = {}
        for index in range(len(nums)):
            if nums[index] not in matchedDictionary:
                matchedDictionary[target - nums[index]] = index
            else:
                return [matchedDictionary[nums[index]], index]

    # def twoSum_bruteForce(self, nums: List[int], target: int) -> List[int]:
    #     for i, iValue in enumerate(nums):
    #         for j, jVale in enumerate(nums):
    #             if i != j and iValue + jVale == target:
    #                 return [i, j]


# leetcode submit region end(Prohibit modification and deletion)


class TestCase(unittest.TestCase):

    def testAddBinary_case1(self):
        nums = [3, 2, 4]
        target = 6
        expectedResult = [1, 2]

        self.assertEqual(Solution().twoSum(nums, target), expectedResult)

    def testAddBinary_case2(self):
        nums = [2, 7, 11, 15]
        target = 9
        expectedResult = [0, 1]

        self.assertEqual(Solution().twoSum(nums, target), expectedResult)

    def testAddBinary_case3(self):
        nums = [0, 3, 3]

        target = 6

        expectedResult = [1, 2]

        self.assertEqual(Solution().twoSum(nums, target), expectedResult)


if __name__ == "__main__":
    unittest.main()

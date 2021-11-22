# Given an array, rotate the array to the right by k steps, where k is non-
# negative. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -2³¹ <= nums[i] <= 2³¹ - 1 
#  0 <= k <= 10⁵ 
#  
# 
#  
#  Follow up: 
# 
#  
#  Try to come up with as many solutions as you can. There are at least three 
# different ways to solve this problem. 
#  Could you do it in-place with O(1) extra space? 
#  
#  Related Topics Array Math Two Pointers 👍 6672 👎 1100


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    # 4 ways to go

    # Approach 1: Brute Force - rotate all the elements of the array in k steps
    # by rotating the elements by 1 unit in each step
    # Comment: Too slow (O(n*k) for Time Complexity and O(1) for Space Complexity)
    # def rotate(self, nums: List[int], k: int) -> None:
    #     shiftTimes = k % len(nums)
    #     for i in range(shiftTimes):
    #         previous = nums[-1]
    #         for j in range(len(nums)):
    #             nums[j], previous = previous, nums[j]

    # Approach 2: Using Extra Array
    # Comment: Unqualified Space Complexity (O(n))
    # def rotate(self, nums: List[int], k: int) -> None:
    #     listLength = len(nums)
    #     toBeReplacedOne = [0] * listLength
    #     for i in range(listLength):
    #         toBeReplacedOne[(i + k) % listLength] = nums[i]
    #     nums[:] = toBeReplacedOne

    # Approach 3: Using Cyclic Replacements (Two Pointers)
    # Store the number being replaced in a temp variable
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # TODO: need to figure it out more
    # def rotate(self, nums: List[int], k: int) -> None:
    #     n = len(nums)
    #     k %= n
    #
    #     start = count = 0
    #     while count < n:
    #         current, prev = start, nums[start]
    #         while True:
    #             next_idx = (current + k) % n
    #             nums[next_idx], prev = prev, nums[next_idx]
    #             current = next_idx
    #             count += 1
    #
    #             if start == current:
    #                 break
    #         start += 1

    # Approach 4:Using Reverse - based on the fact that when we rotate the array k times,
    # k elements from the back end of the array come to the front
    # and the rest of the elements from the front shift backwards
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    class Solution:
        def reverse(self, nums: list, start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1

        def rotate(self, nums: List[int], k: int) -> None:
            n = len(nums)
            k %= n

            self.reverse(nums, 0, n - 1)
            self.reverse(nums, 0, k - 1)
            self.reverse(nums, k, n - 1)

# leetcode submit region end(Prohibit modification and deletion)

# Given an array of non-negative integers nums, you are initially positioned at 
# the first index of the array. 
# 
#  Each element in the array represents your maximum jump length at that positio
# n. 
# 
#  Your goal is to reach the last index in the minimum number of jumps. 
# 
#  You can assume that you can always reach the last index. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 
# step from index 0 to 1, then 3 steps to the last index.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [2,3,0,1,4]
# Output: 2
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 104 
#  0 <= nums[i] <= 1000 
#  
#  Related Topics Array Dynamic Programming Greedy 
#  👍 5494 👎 212


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    # An implicit BFS solution
    def jump(self, nums: List[int]) -> int:
        jumpTimes = 0
        currentEnd = 0
        currentFarthest = 0
        for index in range(len(nums) - 1):
            currentFarthest = max(currentFarthest, index + nums[index])
            if currentFarthest >= len(nums) - 1:
                jumpTimes += 1
                break
            # Like you visited all the items on the current level
            if index == currentEnd:
                # Like incrementing the level you are on
                jumpTimes += 1
                # Like getting the queue size (level size) for the next level you are traversing
                currentEnd = currentFarthest
        return jumpTimes

# leetcode submit region end(Prohibit modification and deletion)

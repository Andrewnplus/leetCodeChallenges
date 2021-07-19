# The median is the middle value in an ordered integer list. If the size of the 
# list is even, there is no middle value and the median is the mean of the two mid
# dle values. 
# 
#  
#  For example, for arr = [2,3,4], the median is 3. 
#  For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5. 
#  
# 
#  Implement the MedianFinder class: 
# 
#  
#  MedianFinder() initializes the MedianFinder object. 
#  void addNum(int num) adds the integer num from the data stream to the data st
# ructure. 
#  double findMedian() returns the median of all elements so far. Answers within
#  10-5 of the actual answer will be accepted. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]
# 
# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
#  
# 
#  
#  Constraints: 
# 
#  
#  -105 <= num <= 105 
#  There will be at least one element in the data structure before calling findM
# edian. 
#  At most 5 * 104 calls will be made to addNum and findMedian. 
#  
# 
#  
#  Follow up: 
# 
#  
#  If all integer numbers from the stream are in the range [0, 100], how would y
# ou optimize your solution? 
#  If 99% of all integer numbers from the stream are in the range [0, 100], how 
# would you optimize your solution? 
#  
#  Related Topics Two Pointers Design Sorting Heap (Priority Queue) Data Stream 
# 
#  👍 4750 👎 85


# leetcode submit region begin(Prohibit modification and deletion)
from heapq import *
import unittest


class MedianFinder:

    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap
        """
        initialize your data structure here.
        """

    # https://docs.python.org/zh-tw/3/library/heapq.html
    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])

    # # Brute Force
    # def __init__(self):
    #     self.array = []
    #     """
    #     initialize your data structure here.
    #     """
    #
    # def addNum(self, num: int) -> None:
    #     self.array.append(num)
    #
    # def findMedian(self) -> float:
    #     self.array.sort()
    #     modulo = divmod(len(self.array), 2)
    #     if modulo[1] == 0:
    #
    #         return (self.array[modulo[0] - 1] + self.array[modulo[0]]) / 2
    #     else:
    #         return self.array[modulo[0]]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# leetcode submit region end(Prohibit modification and deletion)


class TestCase(unittest.TestCase):

    def testStrStr_1(self):
        medianFinder = MedianFinder()

        medianFinder.addNum(1)
        print(medianFinder.findMedian())
        medianFinder.addNum(2)
        print(medianFinder.findMedian())
        medianFinder.addNum(3)
        print(medianFinder.findMedian())


if __name__ == "__main__":
    unittest.main()

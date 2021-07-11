# Design a stack that supports push, pop, top, and retrieving the minimum elemen
# t in constant time. 
# 
#  Implement the MinStack class: 
# 
#  
#  MinStack() initializes the stack object. 
#  void push(val) pushes the element val onto the stack. 
#  void pop() removes the element on the top of the stack. 
#  int top() gets the top element of the stack. 
#  int getMin() retrieves the minimum element in the stack. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# 
# Output
# [null,null,null,null,-3,null,0,-2]
# 
# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
#  
# 
#  
#  Constraints: 
# 
#  
#  -231 <= val <= 231 - 1 
#  Methods pop, top and getMin operations will always be called on non-empty sta
# cks. 
#  At most 3 * 104 calls will be made to push, pop, top, and getMin. 
#  
#  Related Topics Stack Design 
#  👍 4847 👎 453


# leetcode submit region begin(Prohibit modification and deletion)
import sys
import unittest


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        self.stack.append((x, min(self.getMin(), x)))

    def pop(self):
        self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1][0]

    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
        return sys.maxsize


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# leetcode submit region end(Prohibit modification and deletion)

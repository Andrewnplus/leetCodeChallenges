# Given the head of a linked list, remove the nth node from the end of the list 
# and return its head. 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
#  
# 
#  Example 2: 
# 
#  
# Input: head = [1], n = 1
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: head = [1,2], n = 1
# Output: [1]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is sz. 
#  1 <= sz <= 30 
#  0 <= Node.val <= 100 
#  1 <= n <= sz 
#  
# 
#  
#  Follow up: Could you do this in one pass? 
#  Related Topics Linked List Two Pointers 
#  👍 5995 👎 330


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def remove(head, n):
            if head is None:
                return head, 0

            node, count = remove(head.next, n)
            count += 1
            head.next = node

            if count == n:
                head = head.next

            return head, count

        return remove(head, n)[0]
        
# leetcode submit region end(Prohibit modification and deletion)

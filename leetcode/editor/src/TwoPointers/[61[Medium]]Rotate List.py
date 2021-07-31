# Given the head of a linked list, rotate the list to the right by k places. 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
#  
# 
#  Example 2: 
# 
#  
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is in the range [0, 500]. 
#  -100 <= Node.val <= 100 
#  0 <= k <= 2 * 109 
#  
#  Related Topics Linked List Two Pointers 
#  👍 2805 👎 1180


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None:
            return head

        # calculate the length first
        length = 1
        lastElement = head
        while lastElement.next:
            lastElement = lastElement.next
            length += 1
        # Setup the cut one to the head

        # make the linkedList as a circle
        lastElement.next = head
        # determine how many steps we do need to rotate
        rotateTime = k % length
        tempNode = head
        for _ in range(length - rotateTime - 1):
            tempNode = tempNode.next
        result = tempNode.next
        # Cut out the shifted one
        tempNode.next = None

        return result

    # leetcode submit region end(Prohibit modification and deletion)

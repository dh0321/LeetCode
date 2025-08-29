# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head
        while curr:
            next_node = curr.next  # 2 ~ 3 ~ ..
            curr.next = prev  # None
            prev = curr  # 1 ~ None
            curr = next_node  # 2 ~ 3 ~ ..
        return prev

# Iterative
# Time: O(n)
# Space: O(1)

'''
Solution1.
# Recursive
# Time: O(n)
# Space: O(n)

def reverseList(self, head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    if not head or not head.next:
        return head

    new_head = self.reverseList(head.next)
    head.next.next = head  # reverse
    head.next = None
    return new_head

'''

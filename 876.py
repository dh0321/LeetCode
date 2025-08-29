# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        one_step = two_step = head
        while two_step and two_step.next:
            one_step = one_step.next
            two_step = two_step.next.next

        return one_step

# Two Pointers
# Time: O(n)
# Space: O(1)

'''
Solution1.
# Array
# Time: O(n)
# Space: O(n)

def middleNode(self, head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    nodes = []
    while head:
        nodes.append(head)
        head = head.next

    return nodes[len(nodes)//2]


'''
        

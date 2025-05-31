# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        node = head
        first = node
        second = node.next

        while node is not None:
            temp = second.val
            second.val = first.val
            first.val = temp

            if second.next is not None:
                first = second.next
                if second.next.next:
                    second = second.next.next
                else:
                    break
            else:
                break
            
            node = node.next

        return head
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s = set(nums)
        while head is not None and head.val in s:
            head = head.next

        copy = head
    
        while copy.next != None:
            if copy.next.val in s:
                if copy.next.next != None:
                    copy.next = copy.next.next
                else:
                    copy.next = None
            else:
                copy = copy.next

        return head     
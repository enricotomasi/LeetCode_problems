# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:      
        if head == None or head.next == None:
            return head
        
        copy = head
        dup = set()

        last = 101
        
        while copy is not None:
            if copy.val == last:
                dup.add(last)

            last = copy.val
            copy = copy.next

        # print(dup)

        
        while head is not None and head.val in dup:
            head = head.next
        
        if head is None or head.next is None:
            return head
        
        copy = head

        while copy is not None and copy.next is not None:
            # print(copy.next.val)
            while copy.next is not None and copy.next.val in dup:
                copy.next = copy.next.next
            
            copy = copy.next

        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        remove = 0
        copy = head

        while copy != None:
            remove += 1
            copy = copy.next
        
        # print(f"n: {remove}")

        if remove == 1 and n >= 1:
            return None

        remove -= n

        # print(f"Remove: {remove}")

        copy = head
        if remove == 0:
            head = head.next
            return head
    
        for i in range(remove - 1):
            copy = copy.next
        
        if copy.next.next != None:
            copy.next = copy.next.next
        else:
            copy.next = None


        return head
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        copy = head

        less = ListNode(-1)
        great = ListNode(-1)

        l = less
        g = great

        while copy != None:
            # print(f"\n{copy.val}")
            if copy.val < x:
                if l == None:
                    l = ListNode(copy.val)
                else:
                    l.next = ListNode(copy.val)
                    l = l.next
            else:
                if g == None:
                    g = ListNode(copy.val)
                else:
                    g.next = ListNode(copy.val)
                    g = g.next

            # print(f"l: {less}")
            # print(f"g: {great}")
            copy = copy.next
        
        less = less.next
        great = great.next

        l.next = great

        if less == None:
            return great

        return less
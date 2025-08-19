# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        copy = head

        n = 0
        while copy:
            copy = copy.next
            n += 1

        if n <= 1:
            return head
        
        k %= n

        if k == 0:
            return head
        
        # if n == 2:
        #     temp = head.next
        #     head.next = None
        #     temp.next = head
        #     return temp
        
        # print(f"n: {n}")

        point = n - k

        # print(f"point: {point}")

        ans = ListNode()

        second = head

        for i in range(point - 1):
            second = second.next
        
        ok = second.next
        second.next = None

        ans = ok

        while ok.next:
            ok = ok.next
        
        ok.next = head

        return ans
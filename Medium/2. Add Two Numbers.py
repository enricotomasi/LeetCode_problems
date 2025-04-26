# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = False
        first = l1.val + l2.val

        l1 = l1.next
        l2 = l2.next

        if first >= 10:
            carry = True
            first %= 10

        ans = ListNode(first)
        copy = ans


        while l1 != None or l2 != None:
            # print()
            add = 0
            if l1 != None:
                # print(f"l1 exists, {l1.val}")
                add += l1.val
                l1 = l1.next
            if l2 != None:
                # print(f"l1 exists, {l2.val}")
                add += l2.val
                l2 = l2.next
            
            # print(f"sum: {add} carry: {carry}")

            if carry:
                add += 1
                carry = False
            
            if add >= 10:
                carry = True
                add %= 10

            # print(f"sum: {add} carry: {carry}")
            
            copy.next = ListNode(add)
            copy = copy.next
            
        
        if carry:
            copy.next = ListNode(1)
            
        return ans
        
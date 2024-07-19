/**
 * Definition for singly-linked list.
 * struct ListNode
 * {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution
{
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB)
    {
        while (headA)
        {   
            ListNode *copy = headB;

            while (copy)
            {
                if (headA == copy)
                {
                    return headA;
                }
                copy = copy->next;
            }

            headA = headA->next;
        }

        return headA;
    }
};
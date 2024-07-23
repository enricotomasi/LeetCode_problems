/**
 * Definition for singly-linked list.
 * struct ListNode
 * {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution
{
public:
    ListNode* reverseList(ListNode *head)
    {
        auto cur = head;

        ListNode *ans = NULL;
        ListNode *nxt = NULL;

        while (cur)
        {
            nxt = cur->next;
            cur->next = ans;
            ans = cur;
            cur = nxt;
        }

        return ans;
    }
};
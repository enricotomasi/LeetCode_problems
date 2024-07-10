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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) 
    {
        if (!list1 && !list2)
        {
            return NULL;
        }

        if (!list1) return list2;

        if (!list2) return list1;

        ListNode *new1 = NULL;
        ListNode *new2 = NULL;

        if (list1->val > list2->val)
        {
            new1 = list2;
            new2 = list1;
        }
        else
        {
            new1 = list1;
            new2 = list2;
        }
        
        ListNode *ans = new1;

        while (new2)
        {
            if (new1->next && new1->next->val >= new2->val)
            {
                auto n = new1->next;
                
                auto temp = new ListNode(new2->val);

                new1->next = temp;
                new1 = new1->next;
                new1->next = n;
                new2 = new2->next;
            }
            else if (new1->next)
            {
                new1 = new1->next;
            }
            else
            {
                new1->next = new2;
                return ans;
            }

        }

        return ans;
    }
};
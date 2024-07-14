/**
 * Definition for singly-linked list.
 * struct ListNode {
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
    ListNode* deleteDuplicates(ListNode* head) 
    {
        auto ans = head;

        while (head && head->next)
        {
            if (head->val == head->next->val)
            {
                auto temp = head->next;

                while (temp && temp->val == head->val)
                {
                    temp = temp->next;
                }

                if (temp && temp->val != head->val)
                {
                    head->next = temp;
                }
                else
                {
                    head->next = NULL;
                }


            }

            head = head->next;

        }

        return ans;
    }
};
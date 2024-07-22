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
    ListNode* removeElements(ListNode *head, int val)
    {

        while (head && head->val == val)
        {
            head = head->next;
        }

        auto ans = head;

        if (!head)
        {
            return head;
        }
        
        if (!head->next)
        {
            if (head->val == val)
            {
                return NULL;
            }

            return head;
        }

        while (head && head->next)
        {
            // cout << head->val << endl;
            if (head->next->val == val)
            {
                // cout << "remove " << endl;
                auto copy = head->next;

                while (copy && copy->val == val)
                {
                    // cout << "copy " << copy->val << endl;
                    copy = copy->next;
                }

                head->next = copy;
                
            }
            
            head = head->next;
        }

        return ans;
    }
};
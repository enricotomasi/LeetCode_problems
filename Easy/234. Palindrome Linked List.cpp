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
    bool isPalindrome(ListNode *head)
    {
        int n = 0;

        auto copy = head;
        
        while (copy)
        {
            n++;
            copy = copy->next;
        }

        int mid = n / 2;
        cout << "n: " << n << " mid: " << mid << endl;

        ListNode *first = head;
        ListNode *sec = NULL;

        for (int i = 0; i < mid; i++)
        {
            head = head->next;
        }

        if (n % 2 == 0)
        {
            sec = head;
        }
        else
        {
            sec = head->next;
        }
        
        ListNode *prev = NULL;
        ListNode *next = NULL;
        ListNode *curr = sec;

        while (curr)
        {
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }

        auto second = prev;


        while (first && second)
        {
            cout << "first: " << first->val << " second: " << second->val << endl;

            if (first->val != second->val)
            {
                return false;
            }

            first = first->next;
            second = second->next;
        }

        return true;
    }
};
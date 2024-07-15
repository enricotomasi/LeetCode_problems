/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution 
{
public:
    void rec(TreeNode *p, TreeNode *q, bool &ans)
    {
        if (!p && !q)
        {
            return;
        }

        if (!p || !q)
        {
            ans = false;
            return;
        }

        if (p->val != q->val)
        {
            ans = false;
            return;
        }

        rec(p->left, q->left, ans);
        rec(p->right, q->right, ans);

    }
    
    
    bool isSameTree(TreeNode *p, TreeNode *q) 
    {
        bool ans = true;

        rec(p, q, ans);

        return ans;
    }
};
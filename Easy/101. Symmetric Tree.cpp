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
            // cout << "(!p && !q)" << endl;
            return;
        }

        if (!p || !q)
        {
            // cout << "(!p || !q)" << endl;
            ans = false;
            return;
        }

        // cout << p->val << " " << q->val << endl;
        // cout << (!p->left && q->right) << " " << (p->left && !q->right) << " " << (p->left && !q->right) << " " <<
        //         (p->right && !q->left) << " " << (p->left && q->right && p->left->val != q->right->val) << " " <<
        //         (p->right && q->left && p->right->val != q->left->val) << endl;

        if ((!p->left && q->right) ||
            (p->left && !q->right) ||
            (p->left && !q->right) ||
            (p->right && !q->left) ||
            (p->left && q->right && p->left->val != q->right->val) ||
            (p->right && q->left && p->right->val != q->left->val))
        {
            ans = false;
            return;
        }

        rec(p->left, q->right, ans);
        rec(p->right, q->left, ans);

    }
    
    bool isSymmetric(TreeNode* root) 
    {
        if (!root->left && !root->right) return true;
        if (!root->left || !root->right) return false;
        if (root->left->val != root->right->val) return false;
        
        bool ans = true;

        rec(root->left, root->right, ans);

        return ans;   
    }
};
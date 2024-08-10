/**
 * Definition for a binary tree node.
 * struct TreeNode
 * {
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
    int sum(TreeNode *root)
    {
        if (!root)
        {
            return 0;
        }

        return root->val + sum(root->left) + sum(root->right);
    }
    
    void rec(TreeNode * root, int &ans)
    {
        if (!root)
        {
            return;
        }

        ans += abs(sum(root->left) - sum(root->right));

        rec(root->left, ans);
        rec(root->right, ans);
    }
    
    int findTilt(TreeNode *root)
    {
        if (!root)
        {
            return 0;
        }
        
        int ans = 0;

        rec(root, ans);

        return ans;
    }
};
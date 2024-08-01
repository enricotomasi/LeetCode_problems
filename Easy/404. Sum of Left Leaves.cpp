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
    void rec(TreeNode *root, int &ans, bool left)
    {
        if (!root)
        {
            return;
        }

        if (left && !root->left && !root->right)
        {
            ans += root->val;
        }

        rec(root->left, ans, true);
        rec(root->right, ans, false);

    }

    
    int sumOfLeftLeaves(TreeNode *root)
    {
        int ans = 0;

        rec(root, ans, false);

        return ans;
    }
};
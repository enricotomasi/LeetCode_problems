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
    void rec(TreeNode *root, int l, int h, int &ans)
    {
        if (!root)
        {
            return;
        }

        if (root->val >= l && root->val <= h)
        {
            ans += root->val;
        }

        rec(root->left, l, h, ans);
        rec(root->right, l, h, ans);
    }

    int rangeSumBST(TreeNode *root, int low, int high)
    {
        int ans = 0;

        rec(root, low, high, ans);

        return ans;
    }
};
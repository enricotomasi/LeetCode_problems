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

    void rec(TreeNode *root, int &ans)
    {
        if (!root)
        {
            return;
        }

        ans++;

        rec(root->left, ans);
        rec(root->right, ans);

    }

    int countNodes(TreeNode *root)
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
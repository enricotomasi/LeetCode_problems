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
    void rec(TreeNode *root, vector<int> &ans)
    {
        if (!root)
        {
            return;
        }

        rec(root->left, ans);
        ans.push_back(root->val);
        rec(root->right, ans);
    }
    TreeNode *increasingBST(TreeNode *root)
    {
        vector<int> nodes;

        rec(root, nodes);

        TreeNode *ans = new TreeNode(nodes[0]);
        TreeNode *copy = ans;

        for (int i = 1; i < nodes.size(); i++)
        {
            copy->right = new TreeNode(nodes[i]);
            copy = copy->right;
        }

        return ans;

    }
};

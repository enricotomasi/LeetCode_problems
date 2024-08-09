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
    void rec(TreeNode *root, vector<int> &v)
    {
        if (!root)
        {
            return;
        }

        rec(root->left, v);

        v.push_back(root->val);

        rec(root->right, v);
    }
    
    
    int getMinimumDifference(TreeNode *root)
    {
        vector<int> v;
        rec(root, v);

        int n = v.size();
        int ans = INT_MAX;

        for (int i = 0; i < n - 1; i++)
        {
            ans = min(ans, v[i + 1] - v[i]);
        }

        return ans;
    }
};
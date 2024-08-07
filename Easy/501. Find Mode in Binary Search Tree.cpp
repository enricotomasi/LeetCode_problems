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
    void rec(TreeNode *root, unordered_map<int, int> &freq)
    {
        if (!root)
        {
            return;
        }

        freq[root->val]++;

        rec(root->left, freq);
        rec(root->right, freq);
    }

    vector<int> findMode(TreeNode *root)
    {
        unordered_map<int, int> freq;

        rec(root, freq);

        int f = -1;

        for (auto it : freq)
        {
            if (it.second > f)
            {
                f = it.second;
            }
        }

        vector<int> ans;

        for (auto it : freq)
        {
            if (it.second == f)
            {
                ans.push_back(it.first);
            }
        }

        return ans;

    }
};
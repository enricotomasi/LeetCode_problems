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
    void rec(TreeNode *root, unordered_map<int, pair<long long int, long long int>> &m, int level)
    {
        if (!root)
        {
            return;
        }

        // cout << endl << "level: " << level << " data: " << root->val << endl;

        if (m.find(level) != m.end())
        {
            // cout << "exits" << endl;
            m[level] = {m[level].first + root->val, m[level].second + 1};
        }
        else
        {
            // cout << "does not exists" << endl;
            m[level] = {root->val, 1};
        }

        // for (auto it : m) cout << "level: " << it.first << "  --> "<< it.second.first << " / " << it.second.second << endl;

        rec(root->left, m, level + 1);
        rec(root->right, m, level +1);
    }

    vector<double> averageOfLevels(TreeNode *root)
    {
        unordered_map<int, pair<long long int, long long int>> m;

        rec(root, m, 0);

        vector<double> ans;
        int i = 0;

        // cout << endl << "--------------------" << endl;

        while (m.find(i) != m.end())
        {
            // cout << i << "# " << m[i].first << " / " << m[i].second << endl;

            ans.push_back((double)m[i].first / (double)m[i].second);
            i++;
        }

        return ans;
    }
};
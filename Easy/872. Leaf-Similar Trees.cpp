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
    void leafs(TreeNode *root, vector<int> &ans)
    {
        if (!root)
        {
            return;
        }

        if (!root->left && !root->right)
        {
            ans.push_back(root->val);
            return;
        }

        leafs(root->left, ans);
        leafs(root->right, ans);
    }
    
    bool leafSimilar(TreeNode *root1, TreeNode *root2)
    {
        vector<int> one;
        leafs(root1, one);
        
        vector<int> two;
        leafs(root2, two);

        int n = one.size();
        if (n != two.size())
        {
            return false;
        }

        for (int i = 0; i < n; i++)
        {
            if (one[i] != two[i])
            {
                return false;
            }
        }

        return true;
    }
};
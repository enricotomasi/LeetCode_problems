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
    void rec(TreeNode *root, int &ans, int level)
    {
        if (!root)
        {
            return;
        }

        // cout << root->val << " " << level << " " << ans << endl;

        if (!root->left && !root->right)
        {
            // cout << "bingo!" << endl;
            ans = min(ans, level);
        }

        rec(root->left, ans, level + 1);
        rec(root->right, ans, level +1); 
    }
    
    
    int minDepth(TreeNode *root) 
    {
        if (!root)
        {
            return 0;
        }
        
        
        int ans = INT_MAX;

        rec(root, ans, 1);

        return ans;
    }
};
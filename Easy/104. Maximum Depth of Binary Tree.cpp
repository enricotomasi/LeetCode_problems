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
    
    int rec(TreeNode *root, int level)
    {
        if (!root)
        {
            return level;
        }

        return max(rec(root->left, level + 1), rec(root->right, level + 1));
    }

    
    int maxDepth(TreeNode *root)
    {
        if (!root)
        {
            return 0;
        }

        return rec(root, 0);
    }
};
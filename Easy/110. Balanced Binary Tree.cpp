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
    int h(TreeNode *root, int level)
    {
        if (!root)
        {
            return level;
        }

        return max(h(root->left, level + 1), h(root->right, level +1));
        
    }
    
    
    bool isBalanced(TreeNode *root) 
    {
        if (!root || (!root->left && !root->right))
        {
            return true;
        }
        
        int l = h(root->left, 0);
        int r = h(root->right, 0);

        int diff = abs(l - r);

        // cout << "node: " << root->val << " left h: " << l << " right h: " << r << " diff: " << diff << endl;

        if (diff > 1)
        {
            return false;
        }

        return isBalanced(root->left) && isBalanced(root->right);

    }
};
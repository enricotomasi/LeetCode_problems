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
    int rec(TreeNode *root, int temp)
    {
        if (!root)
        {
            return temp;
        }

        return max(rec(root->left, temp + 1), rec(root->right, temp + 1)); 
    }
    
    
    void rec2(TreeNode *root, int &ans)
    {
        if (!root)
        {
            return;
        }

        int l = rec(root->left, 0);
        int r = rec(root->right, 0);

        ans = max(ans, (l + r));

        rec2(root->left, ans);
        rec2(root->right, ans);

    }

    int diameterOfBinaryTree(TreeNode *root)
    {
        int ans = 0;

        rec2(root, ans);

        return ans;
    }
};
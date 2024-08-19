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
    bool search(TreeNode *root, int target)
    {
        if (!root)
        {
            return false;
        }

        // cout << "   Search ->  root->val " << root->val << " target " << target << endl;

        if (root->val == target)
        {
            // cout << "   Search ->  bingo!" << endl;
            return true;
        }
        else if (root->val > target)
        {
            // cout << "   Search ->  left" << endl;
            return search(root->left, target);
        }
        else
        {
            // cout << "   Search ->  right" << endl;
            return search(root->right, target);
        }
    }

    bool rec(TreeNode *root, TreeNode *orig, int k)
    {
        if (!root)
        {
            return false;
        }

        // cout << "REC ->  root->val: " << root->val << " search (k ->root->val): " << (k - root->val) << endl; 
        
        if (k - root->val != root->val && search(orig, k - root->val))
        {
            
            // cout << "REC ->  Bingo!" << endl;
            return true;
        }

        return rec(root->left, orig, k) || rec(root->right, orig, k);
    }
    
    bool findTarget(TreeNode *root, int k)
    {
        if (!root)
        {
            return false;
        }

        return rec(root, root, k);
        
    }
};
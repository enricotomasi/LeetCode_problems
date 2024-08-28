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
    void rec2(TreeNode *root, int val, int &ans)
    {
        if (!root)
        {
            return;
        }

        // cout << "val: " << val << " root->val: " << root->val << " ans: " << ans << endl;
        
        ans = min(ans, abs(val - root->val));
        
        // cout << "  --> new ans: " << ans << endl;

        rec2(root->left, val, ans);
        rec2(root->right, val, ans);
    }    

    void rec(TreeNode *root, int &ans)
    {
        if (!root)
        {
            return;
        }

        int ans2 = ans;
        rec2(root->left, root->val, ans);
        rec2(root->right, root->val, ans);

        rec(root->left, ans);
        rec(root->right, ans);
    }


    int minDiffInBST(TreeNode *root)
    {
        int ans = INT_MAX;

        rec(root, ans);

        return ans;
    }
};
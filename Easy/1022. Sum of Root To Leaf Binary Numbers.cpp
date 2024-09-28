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
    void rec(TreeNode *root, string temp, int &ans)
    {
        if (!root)
        {
            return;
        }
        
        temp += to_string(root->val);

        if (!root->left && !root->right)
        {
            int p = temp.length() - 1;
            int bin = 0;

            for (char c : temp)
            {
                if (c == '1')
                {
                    bin += pow(2, p);
                }

                p--;
            }

            ans += bin;
        }

        rec(root->left, temp, ans);
        rec(root->right, temp, ans);
    }
    
    int sumRootToLeaf(TreeNode *root)
    {
        int ans = 0;
        
        rec(root, "", ans);
        
        return ans;
    }
};
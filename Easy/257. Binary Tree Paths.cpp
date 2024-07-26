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
    void rec(TreeNode *root, set<string> &s, string temp)
    {
        // cout << endl << "temp:" << temp << endl;;
        
        if (!root)
        {
            // cout << "!root" << endl;
            return;
        }

        temp += to_string(root->val);
        
        if (root->left || root->right)
        {
            temp += "->";
        }
        else
        {
            s.insert(temp);
        }

        rec(root->left, s, temp);
        rec(root->right, s, temp);
    }
    
    
    vector<string> binaryTreePaths(TreeNode *root)
    {
        set<string> s;

        rec(root, s, "");

        vector<string> ans;

        for (auto it : s)
        {
            ans.push_back(it);
        }
        
        return ans;
    }
};
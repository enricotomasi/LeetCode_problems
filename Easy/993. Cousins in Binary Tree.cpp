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
    int rec(TreeNode *root, int n, int level)
    {
        if (!root)
        {
            return -1;
        }

        if (root->val == n)
        {
            return level;
        }

        int a = rec(root->left, n, level + 1);
        int b = rec(root->right, n, level + 1);

        if (a < 0) return b;

        return a;

    }

    int par(TreeNode *root, int n, int p)
    {
        if (!root)
        {
            return -1;
        }

        if (root->val == n)
        {
            return p;
        }

        int a = par(root->left, n, root->val);
        int b = par(root->right, n, root->val);

        if (a < 0) return b;
        return a;
    }


    bool isCousins(TreeNode *root, int x, int y)
    {
        int a = rec(root, x, 0);
        int b = rec(root, y, 0);

        int pa = par(root, x, -1);
        int pb = par(root, y, -y);

        // cout << a << ", " << b << endl;
        // cout << pa << ", " << pb << endl;

        return a == b && pa != pb;
    }
};
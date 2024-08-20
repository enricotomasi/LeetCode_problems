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
    int findSecondMinimumValue(TreeNode* root)
    {
        queue<TreeNode*> q;

        q.push(root);

        long  min1 = LONG_MAX;
        long  min2 = LONG_MAX;

        while (!q.empty())
        {
            auto node = q.front();
            q.pop();

            // cout << "node: " << node->val << "  min1: " << min1 << " min2: "  << min2 << endl;

            if (node->val < min2)
            {
                if (node->val <= min1)
                {
                    min1 = node->val;
                }
                else 
                {
                    min2 = node->val;
                }
            }

            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }

        //cout << min2 << endl;
        
        if (min2 == LONG_MAX) return -1;

        return (int)min2;
    }
};
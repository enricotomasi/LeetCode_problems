/*
// Definition for a Node.
class Node
*
{
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val)
    {
        val = _val;
    }

    Node(int _val, vector<Node*> _children)
    {
        val = _val;
        children = _children;
    }
};
*/

class Solution
{
public:
    void rec(Node *root, int temp, int &ans)
    {
        ans = max(ans, temp);   
        if (!root)
        {   
            return;
        }

        //cout << root->val << " temp: " << temp << " ans: " << ans << endl;

        for (auto it : root->children)
        {
             rec(it, temp + 1, ans);
        }

    }
    
    
    int maxDepth(Node *root)
    {
        if (!root)
        {
            return 0;
        }

        int ans = -1;

        rec(root, 1, ans);

        return ans;

    }
};
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
    TreeNode *rec(vector<int>nums, int start, int end)
    {
        if (start > end)
        {
            return NULL;
        }
        
        int mid = (start + end) / 2;

        TreeNode *temp = new TreeNode(nums[mid]);

        temp->left = rec(nums, start, mid - 1);
        temp->right = rec(nums, mid + 1, end);

        return temp;

    }
    
    TreeNode *sortedArrayToBST(vector<int> &nums) 
    {
        if (nums.size() <= 0)
        {
            return NULL;
        }

        int n = nums.size();
        
        int start = 0;
        int end = n - 1;

        int mid = (start + end) / 2;

        TreeNode *ans = new TreeNode(nums[mid]);

        auto copy = ans;
        
        copy->left = rec(nums, start, mid - 1);
        copy->right = rec(nums, mid + 1, end);

        return ans;
    }
};
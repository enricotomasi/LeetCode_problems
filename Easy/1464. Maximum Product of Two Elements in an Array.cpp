class Solution
{
public:
    int maxProduct(vector<int> &nums)
    {
        int n = nums.size();
        sort(nums.begin(), nums.end());

        if (nums[0] >= 0)
        {
             return (nums[n - 1] - 1) * (nums[n - 2] - 1);
        }

        return (nums[0] - 1) * (nums[n - 1] - 1);


    }
};

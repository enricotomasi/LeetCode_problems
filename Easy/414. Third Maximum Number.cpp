class Solution
{
public:
    int thirdMax(vector<int> &nums)
    {
        int n = nums.size();

        sort(nums.begin(), nums.end());

        int ans = nums[n - 1];
        int m = nums[n - 1];
        int index = 0;

        for (int i = n - 1; i >= 0; i--)
        {
            if (index == 2)
            {
                return ans;
            }

            if (nums[i] != ans)
            {
                ans = nums[i];
                index++;
            }
        }

        
        if (index == 2)
        {
            return ans;
        }
        
        return m;
    }
};
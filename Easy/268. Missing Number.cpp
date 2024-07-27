class Solution
{
public:
    int missingNumber(vector<int>& nums)
    {
        int n = nums.size();

        if (n <= 1)
        {
            if (nums[0] == 0)
            {
                return { 1 };
            }
            else
            {
                return { 0 };
            }
        }

        sort(nums.begin(), nums.end());

        if (nums[0] != 0)
        {
            return 0;
        }

        for (int i = 1; i < n; i++)
        {
            cout << nums[i] << " ";
            if (nums[i - 1] != nums[i] - 1)
            {
                return nums[i] - 1;
            }
        }

        return n;
    }
};
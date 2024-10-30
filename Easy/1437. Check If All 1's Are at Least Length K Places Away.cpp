class Solution
{
public:
    bool kLengthApart(vector<int> &nums, int k)
    {
        int n = nums.size();
        int lasti = (k + 1) * -1;

        for (int i = 0; i < n; i++)
        {
            if (nums[i] == 1)
            {
                if (i - lasti <= k)
                {
                    return false;
                }

                lasti = i;
            }
        }

        return true;
        
    }
};

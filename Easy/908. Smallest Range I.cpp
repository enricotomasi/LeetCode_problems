class Solution
{
public:
    int smallestRangeI(vector<int> &nums, int k)
    {
        if (nums.size() == 1)
        {
            return 0;
        }

        int mi = nums[0];
        int ma = mi;

        for (auto it : nums)
        {
            mi = min(mi, it);
            ma = max(ma, it);
        }

        ma -= k;
        mi += k;

        return max(0, (ma - mi));
    }
};

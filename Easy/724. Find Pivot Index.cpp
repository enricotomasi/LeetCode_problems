class Solution
{
public:
    int pivotIndex(vector<int> &nums)
    {
        int n = nums.size();
        int r = 0;

        for (auto it : nums)
        {
            r += it;
        }

        int l = 0;
        int last = 0;
        for (int i = 0; i < n; i++)
        {
            // cout << i << "#  nums[i] = " << nums[i] << " l: " << l << " r:" << r << endl;

            last = nums[i];
            r -= last;
            
            if (l == r)
            {
                return i;
            }

            l += last;

        }

        return -1;
    }
};
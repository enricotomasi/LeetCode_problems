class Solution
{
public:
    int findNumbers(vector<int> &nums)
    {
        int ans = 0;

        for (auto it : nums)
        {
            int digits = (int)log10(it) + 1;
            if (digits % 2 == 0)
            {
                ans++;
            }
        }
        
        return ans;
    }
};

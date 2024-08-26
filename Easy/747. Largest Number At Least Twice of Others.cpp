class Solution
{
public:
    int dominantIndex(vector<int> &nums)
    {
        int n = nums.size();

        int m = INT_MIN;
        int sm = INT_MIN;
        int mi = - 1;


        for (int i = 0; i < n; i++)
        {
            if (sm < nums[i])
            {
                if (m <= nums[i])
                {
                    sm = m;
                    m = nums[i];
                    mi = i;
                }
                else
                {
                    sm = nums[i];
                }
            }
            
            cout << i << "#  nums[i]: " << nums[i] << " max: " << m << " second max: " << sm << endl;

        }

        cout << "end *** " << "max: " << m << " second max: " << sm << " second max * 2: " << (sm * 2) << endl;

        if (sm * 2 <= m)
        {
            return mi;
        }

        return -1;
    }
};
};
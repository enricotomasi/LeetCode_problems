class Solution
{
public:
    vector<int> findErrorNums(vector<int> &nums)
    {
        int n = nums.size();

        if (n == 2)
        {
            if (nums[0] == 1)
            {
                return {1, 2};
            }
            else
            {
                return {2, 1};
            }
        }

        sort(nums.begin(), nums.end());

        int dup = -1;

        for (int i = 0; i < n - 1; i++)
        {
            if (nums[i] == nums[i + 1])
            {
                dup = nums[i];
                break;
            }
        }

        int mis = n;
        int ex = 1;

        for (int i = 0; i < n; i++)
        {
            if (nums[i] != ex)
            {
                if (nums[i] != dup || i == n - 1)
                {
                    mis = ex;
                    break;
                }
            }
            else
            {
                ex++;
            }
        }

        return {dup, mis};

    }
};
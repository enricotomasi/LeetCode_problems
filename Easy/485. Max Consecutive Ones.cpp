class Solution
{
public:
    int findMaxConsecutiveOnes(vector<int> &nums)
    {
        int one = false;
        int ans = 0;
        int temp = 0;

        for (auto it : nums)
        {
            if (it == 1)
            {
                temp++;

                if (!one)
                {
                    one = true;
                }
            }
            else
            {
                one = false;
                ans = max(ans, temp);
                temp = 0;
            }

        }

        return max(ans, temp);

    }
};
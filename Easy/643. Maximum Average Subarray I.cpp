class Solution
{
public:
    double findMaxAverage(vector<int> &nums, int k)
    {
        int n = nums.size();

        int pos = 0;
        double sum = 0;

        for (pos = 0; pos < k; pos++)
        {
            sum += nums[pos];
        }

        double ans = sum / k;

        for (; pos < n; pos++)
        {
            sum -= nums[pos - k];
            sum += nums[pos];

            ans = max(ans, sum / k);
        }

        return ans;
    }
};
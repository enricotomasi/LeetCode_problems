class Solution
{
public:
    int findPoisonedDuration(vector<int> &timeSeries, int duration)
    {
        int n = timeSeries.size();

        if (n == 1)
        {
            return duration;
        }

        int ans = 0;

        for (int i = 0; i < n - 1; i++)
        {
            // cout << endl << i << "#" << endl;
            if (timeSeries[i] + duration - 1 >= timeSeries[i + 1])
            {
                ans += timeSeries[i + 1] - timeSeries[i];
            }
            else
            {
                ans += duration;
            }
        }

        ans += duration;

        return ans;


    }
};
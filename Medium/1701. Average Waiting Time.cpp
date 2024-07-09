
class Solution 
{
public:
    double averageWaitingTime(vector<vector<int>>& customers) 
    {
        vector<int> wt;
        int time = customers[0][0];

        for (auto it : customers)
        {
            int wait = it[1];

            if (time - it[0] > 0)
            {
                wait += time - it[0];
                time += it[1];
            }
            else
            {
                time = it[1] + it[0];
            }

            wt.push_back(wait);

        }

        double ans = 0.0;
        for (auto it : wt)
        {
            ans += it;
        }

        ans /= wt.size();

        return ans;
    }
};
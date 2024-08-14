class Solution
{
public:
    int maxCount(int m, int n, vector<vector<int>> &ops)
    {
        if (ops.size() == 0)
        {
            return m * n;
        }
        
        int a = INT_MAX;
        int b = INT_MAX;

        for (auto it : ops)
        {
            a = min(a, it[0]);
            b = min(b, it[1]);
        }

        return a * b;
    }
};
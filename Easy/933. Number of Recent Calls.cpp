class RecentCounter
{
public:
    vector<int> v;
    int pos = 0;

    RecentCounter()
    {
        v = vector<int>();
        pos = 0;
    }
    
    int ping(int t)
    {
        v.push_back(t);

        int ans = 0;

        for (int i = pos; i < v.size(); i++)
        {
            if (t - v[i] > 3000)
            {
                pos = i;
            }
            else
            {
                ans++;
            }
        }

        return ans;
    }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */
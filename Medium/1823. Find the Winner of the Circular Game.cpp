class Solution  
{
public:
    int findTheWinner(int n, int k) 
    {
        vector<int> v(n, 0);

        for (int i = 1; i <=n; i++)
        {
            v[i - 1] = i;
        }

        int pos = 0;
        while (v.size() > 1)
        {
            pos += k - 1;
            pos %= v.size();

            v.erase(v.begin() + pos);

        }

        return v[0];
    }
};
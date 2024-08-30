class Solution
{
public:
    vector<vector<int>> largeGroupPositions(string s)
    {
        int n = s.length();
        vector<vector<int>> ans;
        
        char last = '*';
        int si = 0;

        for (int i = 0; i < n; i++)
        {
            // cout << i << "# " << s[i] << "  si: " << si << endl;

            if (s[i] != last && last != '*')
            {
                if ((i - si) >= 3)
                {
                    ans.push_back({si, i - 1});
                }
                si = i;
            }
            last = s[i];
        }

        if (n - si >= 3)
        {
            ans.push_back({si, n - 1});
        }
        
        return ans;
    }
};
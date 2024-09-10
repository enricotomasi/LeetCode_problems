class Solution
{
public:
    vector<int> diStringMatch(string s)
    {
        int n = s.length();

        int end = s.length();
        int start = 0;

        vector<int> ans;

        for(int i = 0; i <= n ; i++)
        {
            if (s[i] == 'I')
            {
                ans.push_back(start++);
            }
            else
            {
                ans.push_back(end--);
            }
        }

        return ans;
    }
};

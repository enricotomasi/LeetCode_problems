class Solution
{
public:
    vector<string> commonChars(vector<string> &words)
    {
        int n = words.size();
        vector<vector<int>> v(n, vector<int>(26, 0));

        for (int i = 0; i < n; i++)
        {
            for (char c : words[i])
            {
                v[i][c - 'a']++;
            }
        }

        // for (auto it : v)
        // {
        //     for (auto it2 : it)
        //     {
        //         cout << it2 << " ";
        //     }
        //     cout << endl;
        // }
        
        vector<string> ans;

        for (int i = 0; i < 26; i++)
        {
            int m = INT_MAX;
            
            for (int j = 0; j < n; j++)
            {
                m = min(m, v[j][i]);
            }

            if (m > 0)
            {
                char c = i + 'a';
                for (int k = 0; k < m; k++)
                {
                    string temp = "";
                    temp += c;
                    ans.push_back(temp);
                }
            }
        }

        return ans;
    }
};
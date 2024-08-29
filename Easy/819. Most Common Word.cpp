class Solution
{
public:
    string mostCommonWord(string paragraph, vector<string> &banned)
    {
        set<string> ban(banned.begin(), banned.end());

        unordered_map<string, int> m;

        string temp = "";

        for (auto it : paragraph)
        {
            char c = tolower(it);
            if (c >= 'a' && c <= 'z')
            {
                temp += c;
            }
            else if (temp != "")
            {
                if (ban.find(temp) == ban.end())
                {
                    m[temp]++;
                }
                temp = "";
            }
        }

        if (temp != "")
        {
            m[temp]++;
        }

        int mf = -1;
        string ans = "";
        for (auto it : m)
        {
            if (it.second > mf)
            {
                mf = it.second;
                ans = it.first;
            }
        }

        return ans;
    }
};
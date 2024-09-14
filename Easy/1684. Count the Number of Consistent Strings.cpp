class Solution
{
public:
    int countConsistentStrings(string allowed, vector<string> &words)
    {
        set<char> all;

        for (char c : allowed)
        {
            all.insert(c);
        }

        int ans = 0;

        for (auto it : words)
        {
            bool ok = true;
            for (char c : it)
            {
                if (all.find(c) == all.end())
                {
                    ok = false;
                    break;
                }
            }

            if (ok)
            {
                ans++;
            }
        }

        return ans;
    }
};

class Solution
{
public:
    int countCharacters(vector<string> &words, string chars)
    {
        vector<int> mc(26, 0);
         
        for (char c : chars)
        {
            mc[c - 'a']++;
        }

        int ans = 0;

        for (auto it : words)
        {
            vector<int> copy(mc);
            
            bool ok = true;
            
            for (char c : it)
            {
                copy[c - 'a']--;
                if (copy[c - 'a'] < 0)
                {
                    ok = false;
                    break;
                }
            }

            if (ok)
            {
                ans += it.length();
            }
        }

        return ans;
    }
};
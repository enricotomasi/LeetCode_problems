class Solution
{
public:
    string shortestCompletingWord(string licensePlate, vector<string> &words)
    {
        int nl = licensePlate.size(); 
        int m[26] = { };

        for (int i = 0; i < nl; i++)
        {
            char c = tolower(licensePlate[i]);
            if (c >= 'a' && c <= 'z')
            {
                m[c - 'a']++;
            }
        }

        // for (int i = 0; i < 26; i++) cout << ((char)(i + 'a')) << " " << m[i] << endl;
        
        string ans = "";

        for (auto it : words)
        {
            // cout << endl << it << endl;
            int mw[26] = { };
            for (char c : it)
            {
                mw[c - 'a']++;
            }

            bool ok = true;
            for (int i = 0; i < 26; i++)
            {
                // cout << i << "#  " << ((char)(i + 'a')) << " mw[i]: " << mw[i] << " m[i]: " << m[i] << endl; 
                if (mw[i] < m[i])
                {
                    ok = false;
                    break;
                }
            }

            if (ok)
            {
                if (ans.length() == 0 || ans.length() > it.length())
                {
                    ans = it;
                }
            }
        }

        return ans;
    }
};
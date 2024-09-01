class Solution
{
public:
    bool buddyStrings(string s, string goal)
    {
        int n = s.length();
        if (n != goal.length())
        {
            // cout << "n != goal.length(), return false" << endl;
            return false;
        }
        
        int sm[26] = { };
        for (char c : s)
        {
            sm[c - 'a']++;
        }

        int sg[26] = { };
        for (char c : goal)
        {
            sg[c - 'a']++;
        }

        for (int i = 0; i < 26; i++)
        {
            if (sm[i] != sg[i])
            {
                // cout << "sm[i] != sg[i], number of chars is different, return false" << endl;
                return false;
            }
        }

        int diff = 0;

        for (int i = 0; i < n; i++)
        {
            // cout << i << "#  s[i]: " << s[i]  << " " << (int)s[i] << " --- goal[i]: " << goal[i] << " " << (int)goal[i] << endl;
            if (s[i] != goal[i])
            {
                // cout << "diff!" << endl;
                diff++;
                if (diff > 2)
                {
                    // cout << "diff > 2, return false" << endl;
                    return false;
                }
            }
        }

        // cout << "diff: " << diff << endl;

        if (diff == 0)
        {
            // cout << "No diff!" << endl;
            for (int i = 0; i < 26; i++)
            {
                if (sg[i] >= 2)
                {
                    // cout << "sg[i] >= 2, there are 2 equals chars, return true" << endl;
                    return true;
                }
            }
            // cout << "there are no 2 equals chars, return false" << endl;
            return false;
        }

        // cout << "last ok" << endl;
        return true;


    }
};
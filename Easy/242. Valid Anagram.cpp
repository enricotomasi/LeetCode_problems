class Solution
{
public:
    bool isAnagram(string s, string t)
    {
        int n = s.length();
        
        if (n != t.length())
        {
            return false;
        }
        
        vector<int> sm(26, 0);
        for (auto it : s)
        {
            sm[it - 'a']++;
        }

        vector<int> st(26, 0);
        for (auto it : t)
        {
            st[it - 'a']++;
        }

        for (int i = 0; i < 26; i++)
        {
            //cout << i << "# " << sm[i] << " " << st[i] << endl;
            if (sm[i] != st[i])
            {
                return false;
            } 
        }

        return true;

    }
};
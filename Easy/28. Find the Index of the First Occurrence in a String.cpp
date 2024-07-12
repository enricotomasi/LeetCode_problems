class Solution 
{
public:
    int strStr(string haystack, string needle) 
    {
        string s = haystack;
        string pat = needle;
        
        int n = s.length();
        int np = pat.length();

        for (int i = 0; i < n; i++)
        {
            if (s[i] == pat[0])
            {
                bool ok =  true;
                for (int j = 1; j < np; j++)
                {
                    if (i + j >= n)
                    {
                        return -1;
                    }
                    if (s[i + j] != pat[j])
                    {
                        ok = false;
                        break;
                    }
                }

                if (ok)
                {
                    return i;
                }
            }
        }

        return -1;
    }
};
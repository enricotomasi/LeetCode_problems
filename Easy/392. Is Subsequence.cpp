class Solution
{
public:
    bool isSubsequence(string s, string t)
    {
        int ns = s.length();
        int nt = t.length();

        // cout << "ns: " << ns << " nt: " << nt << endl; 

        if (ns == 0 && nt == 0)
        {
            return true;
        }

        if (ns == 0)
        {
            return true;
        }

        if (nt == 0)
        {
            return false;
        }

        for (int i = 0; i < nt; i++)
        {
            // cout << endl << t[i] << endl;
            if (t[i] == s[0])
            {
                // cout << "bingo i: " << i << endl;
                if (ns == 1)
                {
                    return true;
                }

                int k = 1;
                for (int j = i + 1; j < nt; j++)
                {
                    // cout << "j: " << j << " k: " << k << " t[j]: " << t[j] << " s[k]: " << s[k] << endl;
                    if (k >= ns)
                    {
                        break;
                    }
                    if (t[j] == s[k])
                    {
                        k++;
                    }
                }
                
                // cout << "k:  " << k << " ns - 1:  " << (ns - 1) << endl;
                if (k == ns)
                {
                    return true;
                }
            }

        }


        return false;

    }
};
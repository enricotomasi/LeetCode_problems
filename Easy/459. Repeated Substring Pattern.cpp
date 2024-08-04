class Solution
{
public:
    bool repeatedSubstringPattern(string s)
    {
        int n = s.size();
        
        if (n <= 1)
        {
            return false;
        }

        int mid = floor((double) n / (double) 2);

        for (int i = 1; i <= mid; i++)
        {
            if (n % i != 0)
            {
                // cout << "n % i != 0" << endl;
                continue;
            }

            string sub = s.substr(0, i);

            // cout << endl << "---------------------------------------------" << endl;
            // cout << i << "# " << " substr: " << sub << endl;

            string test = sub;

            for (int j = 0; j < (n / i) - 1; j++)
            {
                test += sub;
            }

            // cout << "test = " << test << endl;

            if (test == s)
            {
                return true;
            }

        }
        
        return false;
    }
};
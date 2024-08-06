class Solution
{
public:
    string licenseKeyFormatting(string s, int k)
    {

        string clean = "";

        for (char c : s)
        {
            if (c != '-')
            {
                if (c >= 'a' && c <= 'z')
                {
                    c -= 32;
                }

                clean += c;
            }
        }

        int n = clean.length();


        string ans = "";
        int pos = (n % k);
        
        // cout << "clean : " << clean << endl;
        // cout << "n     : " << n << endl;
        // cout << "pos   : " << pos << endl;

        if (pos != 0)
        {
            ans = clean.substr(0, pos);
            if (pos < n)
            {
                ans += '-';

            }
        }

        int c = 0;
        while (pos < n)
        {
            // cout << endl << " # pos: " << pos << endl;
            if (c == k)
            {
                ans += '-';
                c = 0;
            }
            else
            {
                ans += clean[pos];
                pos++;
                c++;
            }
        
        }

        return ans;

    }
};
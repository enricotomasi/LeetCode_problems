class Solution
{
public:
    string dec2bin(int n)
    {
        string ans = "";
        
        while (n)
        {
            char c = '1';
            
            if (n % 2 == 0)
            {
                c = '0';
            }
            
            ans = c + ans;
            n /= 2;
            cout << "# " << ans << endl;
        }
        
        return ans;
    }
    
    
    int hammingDistance(int x, int y)
    {
        string sx = dec2bin(x);
        string sy = dec2bin(y);

        // cout << "sx : " << sx << endl << "sy : " << sy << endl;

        int nsx = sx.length();
        int nsy = sy.length();

        int n = max(nsx, nsy);

        // cout << "nsx : " << nsx << endl << "nsy : " << nsy << endl << "n  : " << n << endl;;
        
        if (nsx - nsy != 0)
        {
            int diff = abs(nsx - nsy);
            string str = "";

            for (int i = 0; i < diff; i++)
            {
                str += '0';
            }

            if (nsx > nsy)
            {
                sy = str + sy;
            }
            else
            {
                sx = str + sx;
            }
        }

        // cout << "after padding" << endl;
        // cout << "sx : " << sx << endl << "sy : " << sy << endl;
        
        int ans = 0;

        for (int i = 0; i < n; i++)
        {
            if (sx[i] != sy[i])
            {
                ans++;
            }

        }
        
        return ans;
    }
};
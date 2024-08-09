class Solution
{
public:
    string reverseStr(string s, int k)
    {
        int n = s.length();
        
        if (n < k)
        {
            reverse(s.begin(), s.end());
            return s;
        }
        
        string ans = "";

        bool rev = true;

        int i = 0;

        while (i < n)
        {
            int end = k;
            
            if (end > n)
            {
                end = n - i - 1;
            }
            
            string add = s.substr(i, end);
            
            if (rev)
            {
                reverse(add.begin(), add.end());    
            }
            
            ans += add;
            rev = !rev;
            i += k;
        }

        return ans;
    }
};
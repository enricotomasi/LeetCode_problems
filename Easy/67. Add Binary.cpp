class Solution 
{
public:
    string addBinary(string a, string b) 
    {
        int na = a.length() - 1;
        int nb = b.length() - 1;

        int carry = 0;

        string ans = "";

        while (na >= 0 || nb >= 0)
        {
            
            int first = 0;
            int second = 0;

            if (na >= 0)
            { 
                first =  a[na] - '0';
            }

            if (nb >= 0)
            {
                second = b[nb] - '0';
            }

            int sum = first + second + carry;
            carry = 0;

            if (sum == 0)
            {
                ans = '0' + ans;
            }
            else if (sum == 1)
            {
                ans = '1' + ans;
            }
            else if (sum == 2)
            {
                ans = '0' + ans;
                carry++;
            }
            else
            {
                ans = '1' + ans;
                carry++;
            }
            
            // cout << "na: " << na << " nb:" << nb << " first: " << first << " second: " << second << " carry: " << carry << " ans: " << ans << endl; 

            na--;
            nb--;

        }

        if (carry)
        {
            ans = '1' + ans;
        }
        return ans;
    }
};
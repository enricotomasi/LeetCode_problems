class Solution
{
public:
    string convertToBase7(int num)
    {
        string ans = "";
        bool neg = false;
        
        if (num == 0)
        {
            return "0";
        }
        
        if (num < 0)
        {
            neg = true;
            num *= -1;
        }

        // cout << "num: " << num << endl;
        
        while (num)
        {
            int digit = num % 7;
            digit += '0';
            ans += digit;
            num /= 7;
            // cout << "digit: " << digit << " num: " << num << " ans: " << ans << endl; 
        }    

        if (neg)
        {
            ans += "-";
        }
        
        reverse(ans.begin(), ans.end());

        return ans;
    }
};
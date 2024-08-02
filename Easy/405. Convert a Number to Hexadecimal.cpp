class Solution
{
public:
    string toHex(int num)
    {
        char dic[] = {'0','1','2','3','4', '5', '6', '7', '8', '9', 'a','b','c','d','e','f'};
        long long n = num;
        
        if (n == 0)
        {
            return "0";
        } 
    
        if (n < 0)
        {
            n *= -1;
            n ^= 0xFFFFFFFF;
            n++;
        }
        
        string ans = "";
        
        while (n)
        {
            ans = dic[n % 16] + ans;
            n /= 16;
        }
               
        return ans;
    }
};
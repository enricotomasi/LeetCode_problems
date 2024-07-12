class Solution 
{
public:
    int lengthOfLastWord(string s) 
    {
        int n = s.length();
        int ans = 0;  

        bool start = false;
        for (int i = n - 1; i >= 0; i--)
        {
            if (start)
            {
                if (s[i] == ' ')
                {
                    break;
                }
                
                ans++;
            }
            else
            {
                if (s[i] != ' ')
                {
                    start = true;
                    ans++;
                }
            }

        }

        return ans;
    }
};
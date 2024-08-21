class Solution
{
public:
    int palindrome(string s)
    {
        int start = 0;
        int end = s.length() - 1;
        
        while (start < end)
        {
            if (s[start] != s[end])
            {
                return false;
            }

            start++;
            end--;
        }
        
        return true;
    }

    bool validPalindrome(string s)
    {
        int start = 0; 
        int end = s.length() - 1;
        
        while (start <= end)
        {
            if (s[start] != s[end])
            {
                return palindrome(s.substr(0, start) + s.substr(start + 1)) || palindrome(s.substr(0, end) + s.substr(end + 1));
            }
            
            start++;
            end--;
        }

        return true;  

    }
};
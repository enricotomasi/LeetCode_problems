class Solution
{
    // Hint1: Can you find the primitive decomposition? The number of ( and ) characters must be equal.
public:
    string removeOuterParentheses(string s)
    {
        int par = 0;

        string ans = "";

        for (char c : s)
        {
            if (c == '(')
            {
                if (par > 0) ans += c;
                par++;
            } 
            else 
            {
                par--;
                if (par > 0) ans += c;
            }
        }

        return ans;
    }
};
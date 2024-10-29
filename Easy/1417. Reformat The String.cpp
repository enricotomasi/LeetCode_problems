class Solution
{
public:
    string reformat(string s)
    {
        string dig;
        string let;
        
        for (auto c : s)
        {
            if (isdigit(c))
            {
                dig += c;
            } 
            else
            {
                let += c;
            } 
        }

        int d = dig.size();
        int l = let.size();

        int i = 0;

        if (abs(d - l) > 1)
        {
            return "";
        } 
        
        string ans = "";

        bool digit = true;
        
        if (d < l)
        {
            digit = false;
        } 

        while (i < d and i < l)
        {
            if (digit)
            {
                ans += dig[i];
                ans += let[i];
            }
            else 
            {
                ans += let[i];
                ans += dig[i];
            }
            i++;
        }

        if (d != l)
        {
            if (digit)
            {
                ans += dig.back();
            }
            else
            {
                ans += let.back();
            }
            
        }

        return ans;    
    }
};


class Solution 
{
public:
    string longestCommonPrefix(vector<string>& strs) 
    {
        if (strs.size() == 0)
        {
            return "";
        }
        
        if (strs.size() == 1)
        {
            return strs[0];
        }
        
        
        string ans = "";

        int n = INT_MAX;

        for (auto it : strs)
        {
            int l = it.length();
            n = min(n, l);
        }

        // cout << "MinLenght: " << n << endl;

        for (int i = 0; i < n; i++)
        {
            bool ok = true;
            
            char c = strs[0][i];

            for (auto it : strs)
            {
                if (c != it[i])
                {
                    ok = false;
                    break;
                }
            }

            if (ok)
            {
                ans += c;
            }
            else
            {
                break;
            }

        }


        return ans;    
    }
};
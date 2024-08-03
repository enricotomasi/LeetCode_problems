class Solution
{
public:
    int countSegments(string s)
    {
        bool prespace = true;
        
        int ans = 0;

        for (char c : s)
        {
            if (c != ' ')
            {
                if (prespace)
                {
                    ans++;
                    prespace = false;
                }
            }
            else
            {
                prespace = true;
            }
        }

        return ans;
        

    }
};
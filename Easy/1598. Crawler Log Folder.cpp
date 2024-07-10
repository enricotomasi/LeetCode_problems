class Solution 
{
public:
    int minOperations(vector<string>& logs) 
    {
        int ans = 0;

        for (auto it : logs)
        {
            if (it == "./")
            {
                continue;
            }

            if (it == "../")
            {
                if (ans > 0)
                {
                    ans--;
                }   
            }
            else
            {
                ans++;
            }

            //cout << it << " " << ans << endl;
        }

        return ans;



    }
};
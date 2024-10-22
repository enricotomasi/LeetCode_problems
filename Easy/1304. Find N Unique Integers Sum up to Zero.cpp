class Solution
{
public:
    vector<int> sumZero(int n)
    {
        if (n == 1) return { 0 };

        vector<int> ans;

        bool even = true;
        int d = 1;
        int tot = 0;

        if (n % 2 == 0)
        {
            for (int i = 0; i < n; i++)
            {
                if (even)
                {
                    ans.push_back(d * - 1);
                    tot += d * - 1;
                } 
                else
                {
                    ans.push_back(d);
                    tot += d;
                    d++;
                }
                even = !even;
            }
        }
        else
        {
            ans.push_back(0);
            for (int i = 1; i < n; i++)
            {
                if (even)
                {
                    ans.push_back(d * - 1);
                    tot += d * - 1;
                } 
                else
                {
                    ans.push_back(d);
                    tot += d;
                    d++;
                }
                even = !even;
            }
        }


        // cout << "tot: " << tot << endl;

      

        return ans;
    }
};

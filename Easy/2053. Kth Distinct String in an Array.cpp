class Solution
{
public:
    string kthDistinct(vector<string> &arr, int k)
    {
        unordered_map<string, int> m;

        for (auto it : arr)
        {
            m[it]++;
        }

        k--;

        for (auto it : arr)
        {
            // cout << it << " " << m[it] << " k: " << k << endl;
            if (m[it] == 1)
            {
                if (k > 0)
                {
                    k--;
                }
                else
                {
                    return it;
                }
            }
        }

        return "";

        
    }
};
class Solution
{
public:
    vector<string> findRelativeRanks(vector<int> &score)
    {
        int n = score.size();
        
        vector<int> copy(score.begin(), score.end()); 
        sort(copy.begin(), copy.end());

        unordered_map<int, string> m;

        int count = 1;
        for (int i = n - 1; i >= 0; i--)
        {
            if (count == 1)
            {
                m[copy[i]] = "Gold Medal";
            }
            else if (count == 2)
            {
                m[copy[i]] = "Silver Medal";
            }
            else if (count == 3)
            {
                m[copy[i]] = "Bronze Medal";
            }
            else
            {
                m[copy[i]] = to_string(count);
            }

            count++;
        }

        vector<string> ans;

        for (int i = 0; i < n; i++)
        {
            ans.push_back(m[score[i]]);
        }

        return ans;
    }
};
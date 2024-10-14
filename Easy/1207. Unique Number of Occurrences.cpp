class Solution
{
public:
    bool uniqueOccurrences(vector<int> &arr)
    {
        unordered_map<int, int> freq;

        for (auto it : arr)
        {
            freq[it]++;
        }

        unordered_set<int> s;
        for (auto it : freq)
        {
            if (s.find(it.second) != s.end())
            {
                return false;
            }

            s.insert(it.second);       
        }

        return true;

    }
};

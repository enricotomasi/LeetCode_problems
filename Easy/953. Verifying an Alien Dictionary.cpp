class Solution
{
public:
    bool isAlienSorted(vector<string> &words, string order)
    {
        map<char, int> d;
        
        for (int i = 0; i < order.size(); i++)
        {
            d[order[i]] = 'a' + i;
        }
        
        for (int i = 0; i < words.size(); i++)
        {
            for (int j = 0; j < words[i].size(); j++)
            {
                words[i][j] = d[words[i][j]];
            }
        }

        return is_sorted(words.begin(), words.end());
    }
};

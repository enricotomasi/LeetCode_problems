class Solution
{

// Hint 1: Split the string into words, then look at adjacent triples of words.

public:
    vector<string> findOcurrences(string text, string first, string second)
    {
        vector<string> v;
        
        string w = "";
 
        for (char c : text)
        {
            if (c == ' ')
            {
                v.push_back(w);
                w = "";
            }
            else
            {
                 w += c;
            }
        }

        v.push_back(w);
        
        vector<string> ans;
        
        int n = v.size() - 2;

        for (int i = 0; i < n; i++)
        {
            if (v[i] == first && v[i + 1] == second)
            {
                ans.push_back(v[i + 2]);
            }

        }
        
        return ans;     
    }
};

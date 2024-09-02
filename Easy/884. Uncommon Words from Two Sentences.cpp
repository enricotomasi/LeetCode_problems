class Solution
{
public:
    unordered_map<string, int> sm(string s)
    {
        unordered_map<string, int> ans;

        string temp = "";
        for (char c : s)
        {
            if (c == ' ')
            {
                // cout << temp << endl; 
                ans[temp]++;
                temp = "";
            }
            else
            {
                temp += c;
            }
        }

        if (temp != "")
        {
            ans[temp]++;
        }

        return ans;

    }

    
    vector<string> uncommonFromSentences(string s1, string s2)
    {
        unordered_map<string, int> m1 = sm(s1);
        unordered_map<string, int> m2 = sm(s2);
        
        vector<string> ans;
        
        for (auto it : m1)
        {
           
            if (it.second == 1 && m2.find(it.first) == m2.end())
            {
                ans.push_back(it.first);
            }
        }

        for (auto it : m2)
        {
           
            if (it.second == 1 && m1.find(it.first) == m1.end())
            {
                ans.push_back(it.first);
            }
        }

        return ans;

    }
};

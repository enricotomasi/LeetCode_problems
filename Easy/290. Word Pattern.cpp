class Solution
{
public:
    bool wordPattern(string pattern, string s)
    {
        vector<string> words;
        string temp = "";

        for (char c : s)
        {
            if (c == ' ')
            {
                words.push_back(temp);
                temp = "";
            }
            else
            {
                temp += c;
            }
        }

        words.push_back(temp);

        // cout << endl << "words.size(): " << words.size() << endl;
        // for (auto it : words) cout << it << " # ";
        // cout << endl;

        int n = pattern.length();

        if (n != words.size())
        {
            return false;
        }

        unordered_map<char, string> m;

        for (int i = 0; i < n; i++)
        {
            if (m.find(pattern[i]) == m.end())
            {
                for (auto it : m)
                {
                    if (it.second == words[i])
                    {
                        return false;
                    }
                }
                m[pattern[i]] = words[i];
            }
            else if (m[pattern[i]] != words[i])
            {
                // cout << i << " exit! pattern[i]: " << pattern[i] << " m[pattern[i]]: " << m[pattern[i]] << " words[i]: " << words[i] << endl;
                return false;
            }
            else
            {
                // cout << i << " OK ***  pattern[i]: " << pattern[i] << " m[pattern[i]]: " << m[pattern[i]] << " words[i]: " << words[i] << endl;
            }
            
            // cout << endl;
            // for (auto it : m) cout << it.first << "  =  " << it.second << endl;
            // cout << endl;

        }

        return true;
    }
};
class Solution
{
public:
    vector<string> findWords(vector<string> &words)
    {
        unordered_set<char> first = { 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p' };
        unordered_set<char> second = { 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'};
        unordered_set<char> third = { 'z', 'x', 'c', 'v', 'b', 'n', 'm'};

        vector<string> ans;

        for (auto it : words)
        {
            string word = it;
            transform(it.begin(), it.end(), it.begin(), ::tolower);
            
            int n = it.length();
            if (n == 1)
            {
                ans.push_back(it);
                continue;
            }

            int row = -1;
            
            if (first.find(it[0]) != first.end()) row = 0;
            if (second.find(it[0]) != second.end()) row = 1;
            if (third.find(it[0]) != third.end()) row = 2;

            // cout << endl << "word: " << word << " ---- row: " << row << endl;
            // cout << " -> : ";

            bool ok = true;

            for (int i = 1; i < n; i++)
            {
                // cout << it[i];

                if (row == 0)
                {
                    if (first.find(it[i]) == first.end())
                    {
                        ok = false;
                        break;
                    }
                }
                else if (row == 1)
                {
                    if (second.find(it[i]) == second.end())
                    {
                        ok = false;
                        break;
                    }
                }
                else
                {
                    if (third.find(it[i]) == third.end())
                    {
                        ok = false;
                        break;
                    }
                }
            }

            // cout << endl;

            if (ok)
            {
                ans.push_back(word);
            }
        }

        return ans;
    }
};
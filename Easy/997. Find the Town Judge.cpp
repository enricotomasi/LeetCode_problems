class Solution
{
public:
    int findJudge(int n, vector<vector<int>> &trust)
    {
        if (trust.size() == 0 && n > 1)
        {
            return -1;
        }

        unordered_map<int, unordered_set<int>> t;

        for (auto it : trust)
        {
            if (t.find(it[0]) != t.end())
            {
                t[it[0]].insert(it[1]);
            }
            else
            {
                unordered_set<int> temp = {it[1]};
                t[it[0]] = temp;
            }
        }
        
        // for (auto it : t)
        // {
        //     cout << it.first << " : ";
        //     for (auto it2 : it.second) cout << it2 << " ";
        //     cout << endl;
        // }

        if (t.size() != n - 1)
        {
            return -1;
        }

        for (int i = 1; i <= n; i++)
        {
            if (t.find(i) == t.end())
            {
                bool ok = true;
                for (auto it : t)
                {
                    if (it.second.find(i) == it.second.end())
                    {
                        ok = false;
                        break;
                    }
                }

                if (ok)
                {
                    return i;
                }
            }
        }

        return -1;

    }
};
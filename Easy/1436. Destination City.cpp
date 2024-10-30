class Solution
{
public:
    string destCity(vector<vector<string>> &paths)
    {
        unordered_set<string> cities;

        for (auto it : paths)
        {
            cities.insert(it[0]);
            cities.insert(it[1]);
        }

        for (auto it : paths)
        {
            auto f = cities.find(it[0]);
            if (f != cities.end())
            {
                cities.erase(f);
            }
        }

        return *cities.begin();

    }
};

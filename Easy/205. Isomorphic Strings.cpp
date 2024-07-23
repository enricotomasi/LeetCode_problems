class Solution
{
public:
    bool isIsomorphic(string s, string t)
    {
        int n = s.length();

        if (n != t.length())
        {
            return false;
        }
        
        map<char,int> map1;
        map<char,int> map2;

        for (auto it : s)
        {
            map1[it]++;
        }

        for (auto it : t)
        {
            map2[it]++;
        }

        vector<int> vec1;
        vector<int> vec2;

        for (auto it : map1)
        {
            vec1.push_back(it.second);
        }

        for (auto it : map2)
        {
            vec2.push_back(it.second);
        }

        sort(vec1.begin(), vec1.end());
        sort(vec2.begin(), vec2.end());

        if (vec1 != vec2)
        {
            return false;
        }

        unordered_map<char, char> map_gen;

        for (int i = 0; i < n; i++)
        {
            map_gen[s[i]] = t[i];
        }

        for (int i = 0; i < n; i++)
        {
            if (map_gen[s[i]] != t[i])
            {
                return false;
            }
        }

        return true;
    }
};
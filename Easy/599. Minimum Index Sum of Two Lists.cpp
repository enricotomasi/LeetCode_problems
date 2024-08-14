class Solution
{
public:
    static bool cmp(pair<string, int> &a, pair<string, int> b)
    {
        return a.second < b.second;
    }
    
    vector<string> findRestaurant(vector<string> &list1, vector<string> &list2)
    {
        int n1 = list1.size(); 
        int n2 = list2.size();

        if (n1 == 0 || n2 == 0)
        {
            return { };
        }

        unordered_map<string, int> a2;

        for (int i = 0; i < n2; i++)
        {
            a2[list2[i]] = i;
        }

        int minind = -1;

        vector<pair<string, int>> m;
        for (int i = 0; i < n1; i++)
        {
            if (a2.find(list1[i]) != a2.end())
            {
                m.push_back({list1[i] ,(a2[list1[i]] + i)}); 
            }
        }

        sort(m.begin(), m.end(), cmp);

        int ind = -1;

        vector<string> ans;
        for (auto it : m)
        {
            if (ind < 0)
            {
                ans.push_back(it.first);
                ind = it.second;
            }
            else if (it.second == ind)
            {
                 ans.push_back(it.first);
            }
            else
            {
                break;
            }
        }


        return ans;
    }
};
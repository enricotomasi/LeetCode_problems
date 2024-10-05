class Solution
{
public:
    vector<int> distributeCandies(int candies, int num_people)
    {
        vector<int> ans(num_people, 0);

        int pos = 0;
        int i = 1;
        while (candies > 0)
        {
            if (i <= candies)
            {
                ans[pos] += i;
                candies -= i;
            }
            else
            {
                ans[pos] += candies;
                break;
            }
            pos++;
            pos %= num_people;
            i++;
            
            // for (auto it : ans) cout << it << " ";
            // cout << "    candies: " << candies << endl;

        }

        return ans;
    }
};
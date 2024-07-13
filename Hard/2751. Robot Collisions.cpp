class Solution 
{
public:
    vector<int> survivedRobotsHealths(vector<int>& positions, vector<int>& healths, string directions) 
    {
        int n = positions.size();
        vector<pair<int, int>> map;

        for (int i = 0; i < n; i++)
        {
            map.push_back({positions[i], i});
        }

        sort(map.begin(), map.end());
        
        stack<int> stack;
        stack.push(map[0].second);
        
        for (int i = 1; i < map.size(); i++) 
        {
            int sec = map[i].second;
            
            if (!stack.empty())
            {
                int curr = stack.top();

                if (directions[sec] == 'L' && directions[curr] == 'R')
                {
                    if (healths[sec] > healths[curr])
                    {
                        healths[sec]--;
                        stack.pop();
                        i--;
                    }
                    else if (healths[sec] < healths[curr])
                    {
                        healths[curr]--;
                    }
                    else
                    {
                        stack.pop();
                    }
                }
                else
                {
                    stack.push(sec);
                }
            }
            else
            {
                stack.push(sec);
            } 
        }
        
        vector<int> ans;

        while (!stack.empty()) 
        {
            ans.push_back(stack.top());
            stack.pop();
        }

        sort(ans.begin(), ans.end());
        
        for (int i = 0; i < ans.size(); i++) 
        {
            ans[i] = healths[ans[i]];
        }

        return ans;
    }
};
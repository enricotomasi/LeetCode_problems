class Solution
{
public:
    vector<int> shortestToChar(string s, char c)
    {
        int n = s.length();
        queue<int> car;

        for (int i = 0; i < n; i++)
        {
            if (s[i] == c)
            {
                // cout << i << " ";
                car.push(i);
            }
        }

        int last = -999999;
        // cout << endl;

        vector<int> ans;
        for (int i = 0; i < n; i++)
        {
            // cout << endl << i << "#  last:" << last << " car.empty(): " << car.empty() << endl;
            if (car.empty() || abs(i - last) < abs(i - car.front()))
            {
                // cout << "abs(i - last): " << abs(i - last) << endl;
                ans.push_back(abs(i - last));
            }
            else
            {
                // cout << "car.front(): " << car.front() << " abs(car.front() - i): " << abs(car.front() - i) << endl;
                ans.push_back(abs(car.front() - i));
                last = car.front();
                car.pop();
            }
        }

        return ans;
    }
};
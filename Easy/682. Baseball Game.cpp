class Solution
{
public:
    int calPoints(vector<string> &operations)
    {
        stack<long> s;

        for (auto it : operations)
        {
            // cout << endl << "operation: " << it << endl;
            
            if (it == "+")
            {
                long last1 = s.top();
                s.pop();
                
                long last2 = 0;
                bool second = false;
                if (!s.empty())
                {
                    second = true;
                    last2 = s.top();
                    s.pop();
                }

                if (second)
                {
                    s.push(last2);
                }

                s.push(last1);

                s.push(last1 + last2);
            }
            
            else if (it == "D")
            {
                s.push(s.top() * 2);
            }
            
            else if (it == "C")
            {
                s.pop();
            }

            else 
            {
                long temp = stol(it);
                s.push(temp);
            }

            // stack<long> debug(s);
            // while (!debug.empty())
            // {
            //     cout << debug.top() << " ";
            //     debug.pop();
            // }
            // cout << endl; 
            
        }

        long ans = 0;

        while (!s.empty())
        {
            ans += s.top();
            s.pop();
        }

        return (int)ans;
    }
};
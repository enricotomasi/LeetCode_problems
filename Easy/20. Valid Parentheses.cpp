class Solution 
{
public:
    bool isValid(string s) 
    {
        stack<char> st;

        for (auto c : s)
        {
            // cout << "c: " << c << " st.size: " << st.size() << endl;
            if (c == '(' || c == '[' || c == '{')
            {
                st.push(c);
            }            
            else if (c == ')')
            {
                // cout << "st.top: " << st.top() << endl;
                if (st.empty() || st.top() != '(')
                {
                    return false;
                } 
                else
                {
                    st.pop();
                } 
            }
            else if (c == ']')
            {
                // cout << "st.top: " << st.top() << endl;
                if (st.empty() || st.top() != '[')
                {
                    return false;
                }
                else
                {
                    st.pop();
                }   
            }
            else if (c == '}')
            {
                // cout << "st.top: " << st.top() << endl;
                if (st.empty() || st.top() != '{')
                {
                    return false;
                } 
                else
                {
                    st.pop();
                }    
            }
        }

        // cout << st.size() << endl;

        return st.empty();

    }
};
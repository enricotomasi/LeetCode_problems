class Solution 
{
public:
    int maximumGain(string s, int x, int y) 
    {
        vector<char> st;
        int ans = 0;

        for (char c : s) 
        {
            if (!st.empty()) 
            {
                if (x > y) 
                {
                    if (st.back() == 'a' && c == 'b') 
                    {
                        ans += x;
                        st.pop_back();
                    } 
                    else
                    {
                        st.push_back(c);
                    }
                }
                else 
                {
                    if (st.back() == 'b' && c == 'a') 
                    {
                        ans += y;
                        st.pop_back();
                    } 
                    else
                    {
                        st.push_back(c);
                    }
                        
                }
            }
            else
            {
                st.push_back(c);
            }
        }

        vector<char> st2;

        for (char c : st)
            if (!st2.empty()) 
            {
                if (x < y) 
                {
                    if (st2.back() == 'a' && c == 'b')
                    {
                        ans += x;
                        st2.pop_back();
                    }
                    else
                    {
                        st2.push_back(c);
                    }
                }
                else 
                {
                    if (st2.back() == 'b' && c == 'a') 
                    {
                        ans += y;
                        st2.pop_back();
                    } 
                    else
                    {
                        st2.push_back(c);
                    }
                }
            }
            else
            {
                st2.push_back(c);
            }

        return ans;
    }

};
class MyQueue
{
public:
    stack<int> s;
    MyQueue()
    {
        s = stack<int>();
    }
    
    void push(int x)
    {
        if (s.size() == 0)
        {
            s.push(x);
            return;
        }

        stack<int> temp;

        while (!s.empty())
        {
            temp.push(s.top());
            s.pop();
        }

        s.push(x);

        while (!temp.empty())
        {
            s.push(temp.top());
            temp.pop();
        }

    }
    
    int pop()
    {
        if (s.empty())
        {
            return -1;
        }
        
        stack<int> temp;

        int ans = s.top();
        s.pop();

        while (!s.empty())
        {
            temp.push(s.top());
            s.pop();
        }

        while (!temp.empty())
        {
            s.push(temp.top());
            temp.pop();
        }

        return ans;
    }
    
    int peek()
    {
        if (s.empty())
        {
            return -1;
        }
        
        stack<int> temp;

        int ans = s.top();
        //s.pop();

        while (!s.empty())
        {
            temp.push(s.top());
            s.pop();
        }

        while (!temp.empty())
        {
            s.push(temp.top());
            temp.pop();
        }

        return ans;
    }
    
    bool empty()
    {
        return s.empty();
    }

};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */